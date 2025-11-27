from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.models import User

from .serializers import RegisterSerializer

from transformers import pipeline
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Carrega o modelo de IA uma única vez ao iniciar o servidor
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Gera token JWT na hora do registro
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

class SummarizeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get('text', '')

        if not text.strip():
            return Response(
                {"detail": "Campo 'text' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Chamando modelo local
        try:
            result = summarizer(
                text,
                max_length=130,
                min_length=30,
                do_sample=False
            )
            summary_text = result[0]['summary_text']
        except Exception as e:
            return Response(
                {"detail": f"Erro ao gerar resumo: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"summary": summary_text}, status=status.HTTP_200_OK)
