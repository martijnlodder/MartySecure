import socket
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vulnerability

from rest_framework import generics
from .serializers import ValidatedResultSerializer
from .models import ValidatedResult


class ValidatedResultList(generics.ListAPIView):
    queryset = ValidatedResult.objects.all()
    serializer_class = ValidatedResultSerializer


def index(request):
    return render(request, 'base.html', {})


def port_scan(request):
    host = '127.0.0.1'  # IP-adres om te scannen
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
    return render(request, 'port_scan.html', context)


def banner_grabbing(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
    banner = s.recv(1024).decode()
    s.close()
    return banner


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
