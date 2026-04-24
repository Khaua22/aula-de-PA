{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPCFChnE8gkZqdY3zZSsIZj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Khaua22/aula-de-PA/blob/main/aula%20dia%2024/04/2026.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VrV-okgIBTrH",
        "outputId": "16572a09-75e8-4d26-8a2c-111dabb84d25"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "olá mundo !\n",
            "olá mundo !\n",
            "olá mundo !\n",
            "olá mundo !\n",
            "olá mundo !\n"
          ]
        }
      ],
      "source": [
        "# Loops  - laços e oterações\n",
        "\n",
        "for i in range(5):\n",
        "  print (\"olá mundo !\")\n",
        ""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Loops  - laços e oterações\n",
        "\n",
        "for i in range(5):\n",
        "  print (i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G68Bm_n5D86d",
        "outputId": "a1eadf59-9293-406c-bac9-7bef177923b6"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Escrever um progama que recebe um numero e retorna um numero somente os numeros pares\n",
        "\n",
        "numero = int (input(\"digie um número: \"))\n",
        "\n",
        "for i in range(numero+1) :\n",
        " if i % 2 ==0:\n",
        "  print (i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6QX3yomhEQzk",
        "outputId": "f793d765-3c78-4502-f801-c7509337954c"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digie um número: 20\n",
            "0\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Escrever um programa que recebe um numero e imprimi ao contrario\n",
        "\n",
        "numero = int(input(\"digite um numero: \"))\n",
        "\n",
        "for i in range(numero +1):\n",
        "  print(numero - i)\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aZwpT5cuGXgZ",
        "outputId": "6e8a1854-02df-4940-a074-25af5daf9cef"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite um numero: 20\n",
            "20\n",
            "19\n",
            "18\n",
            "17\n",
            "16\n",
            "15\n",
            "14\n",
            "13\n",
            "12\n",
            "11\n",
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "palavra = \"pyton\"\n",
        "\n",
        "for i in (\"pyton\"):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rz2KKxyIIPxN",
        "outputId": "d080e5ee-8a5c-4be9-bef2-f95c775d0260"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "p\n",
            "y\n",
            "t\n",
            "o\n",
            "n\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "palavra = (input(\"dite uma palavra\"))\n",
        "palindromo = \"\"\n",
        "\n",
        "for i in (palavra):\n",
        "  palindromo = i + palindromo\n",
        "print(palindromo)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9FVGgRjTKdHj",
        "outputId": "a4e3a770-d6e4-45fc-8718-cc90d95b78e7"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dite uma palavraroma\n",
            "amor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Escrever um programa que recebe um numero de um a 10 e imprimi a tabuada.\n",
        "\n",
        "numero = int(input(\"Digite um número de 1 a 10 : \"))\n",
        "\n",
        "for i in range (1, 11):\n",
        "  print (f \"{numero} x {i} = {numero * i}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "lrw41zcsQumU",
        "outputId": "0db0257e-9d0b-4698-98c7-0196bff8cfcf"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (2948874620.py, line 6)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_9959/2948874620.py\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    print (f \"{numero} x {i} = {numero * i}\")\u001b[0m\n\u001b[0m             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Escrever um programa que recebe um numero de um a 10 e imprimi a tabuada.\n",
        "\n",
        "numero = int(input(\"Digite um número de 1 a 10 : \"))\n",
        "\n",
        "if 1 <= numero <= 10:\n",
        "  print(f\"Tabuada do {numero}:\")\n",
        "  for i in range(1, 11):\n",
        "    print(f\"{numero} x {i} = {numero * i}\")\n",
        "elif numero < 1:\n",
        "  print(\"O número deve ser maior que 0.\")\n",
        "else:\n",
        "  print(\"O número deve ser menor ou igual a 10.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qVp4Gd66OC10",
        "outputId": "b32981e6-7492-4b74-98ac-d0a28c50a48e"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número de 1 a 10 : 4\n",
            "Tabuada do 4:\n",
            "4 x 1 = 4\n",
            "4 x 2 = 8\n",
            "4 x 3 = 12\n",
            "4 x 4 = 16\n",
            "4 x 5 = 20\n",
            "4 x 6 = 24\n",
            "4 x 7 = 28\n",
            "4 x 8 = 32\n",
            "4 x 9 = 36\n",
            "4 x 10 = 40\n"
          ]
        }
      ]
    }
  ]
}