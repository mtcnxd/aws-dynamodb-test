import boto3
from config import *
import flet as ft

ec2 = boto3.client(
    'ec2', 
    region_name='us-east-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

def start_instance():
    try:
        response = ec2.start_instances(InstanceIds=[aws_instance_id])
        print(f"Comando enviado correctamente: {response}")

    except Exception as e:
        print(e)

def stop_instance():
    try:
        response = ec2.stop_instances(InstanceIds=[aws_instance_id])
        print(f"Comando enviado correctamente: {response}")

    except Exception as e:
        print(e)

def aws_controll_instance(page: ft.Page):
    page.title = "AWS Controll Instance"
    page.window.width = 400
    page.window.height = 200
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.Row([
            ft.FilledButton("Iniciar Instancia", on_click=start_instance),
            ft.FilledButton("Detener Instancia", on_click=stop_instance)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=aws_controll_instance)