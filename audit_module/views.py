import os
from django.shortcuts import render
from django.utils.decorators import method_decorator
from multifactor.decorators import multifactor_protected
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view


class LogsAuditView(APIView):
    permission_classes = [AllowAny]

    @method_decorator(
        multifactor_protected(factors=1, user_filter=None, advertise=False),
        name="get_logs",
    )
    def get(self, request):
        print("get", request.__dict__)
        print("request.user", request.user.__dict__)
        logs_path = "/app/logs/"
        print(os.listdir("/app/audit_module/templates/"))
        log_files = os.listdir(logs_path)
        logs = []

        for log_file in log_files:
            with open(os.path.join(logs_path, log_file), "r") as file:
                log_content = file.read()
                logs.append({"filename": log_file, "content": log_content})

        return render(request, "logs_view.html", {"logs": logs})
