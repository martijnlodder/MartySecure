import socket
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vulnerability

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ValidatedResultSerializer
from .models import ValidatedResult

import requests
from django.core.mail import send_mail
from django.conf import settings

class ValidatedResultList(generics.ListAPIView):
    queryset = ValidatedResult.objects.all()
    serializer_class = ValidatedResultSerializer


def index(request):
    return render(request, 'base.html', {})


def port_scan(request):
    host = 'google.com'  # IP-adres om te scannen
    ports = [22, 21, 53, 80, 443, 8080]  # Poorten om te scannen
    results = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            banner = banner_grabbing(host, port)
            results.append({'port': port, 'status': 'Open', 'banner': banner})
        except:
            results.append({'port': port, 'status': 'Dicht', 'banner': ''})
        s.close()

    send_results_by_email(results)

    context = {'results': results}
    return render(request, 'port_scan.html', context)


def port_scan_api(target):
    host = target  # IP-adres om te scannen
    ports = [80, 443, 8080]  # Poorten om te scannen
    results = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            banner = banner_grabbing(host, port)
            results.append({'port': port, 'status': 'Open', 'banner': banner})
        except:
            results.append({'port': port, 'status': 'Dicht', 'banner': ''})
        s.close()

    context = {'results': results}
    return render(target, 'port_scan.html', context)


def banner_grabbing(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
    banner = s.recv(1024).decode()
    s.close()
    return banner

class PortScanAPIView(APIView):
    def get(self, request):
        host = request.query_params.get('host')
        # Voer hier de poortscan uit en valideer de resultaten
        # Stel de gevalideerde resultaten in op de variabele 'validated_results'

        validated_results = [
            # Voorbeeld van gevalideerde resultaten
            {
                'port': 80,
                'service': 'HTTP',
                'version': '1.1',
                'vulnerability': 'Not Detected',
                'description': 'None',
                'severity': 'None',
            },
            # ... voeg andere gevalideerde resultaten toe ...
        ]

        return Response(validated_results)


def validate_results(results):
    vulnerabilities = Vulnerability.objects.all()
    validated_results = []

    for result in results:
        for vulnerability in vulnerabilities:
            if (result['service'] in vulnerability.services.split(',') and
                    result['version'] == vulnerability.version):
                validated_results.append({
                    'port': result['port'],
                    'service': result['service'],
                    'version': result['version'],
                    'vulnerability': vulnerability.name,
                    'description': vulnerability.description,
                    'severity': vulnerability.severity
                })

    return validated_results


def format_results(results):
    text = ""
    for result in results:
        text += f"- Port {result['port']}: {result['status']}\n"
    return text


def send_results_by_email(results):
    formatted_results = format_results(results)

    # Verstuur e-mail via Mailgun API
    url = f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages"
    auth = ("api", settings.MAILGUN_API_KEY)
    recipient = "500334@student.fontys.nl"
    subject = "Portscan Results"
    content = "Here are the results of the port scan:\n\n" + formatted_results

    data = {
        "from": settings.MAILGUN_SENDER,
        "to": recipient,
        "subject": subject,
        "text": content
    }

    response = requests.post(url, auth=auth, data=data)

    if response.status_code == 200:
        print("The port scan results have been send succesfully.")
    else:
        print("An error occured while sending the results!")