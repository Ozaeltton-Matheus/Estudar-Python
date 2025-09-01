from InquirerPy import prompt
perguntas = [
    {
        "type": "list",
        "mensage": "Qual seu conhecimento em PCs?"
        "choices": ["Iniciante","Intermédiario", "Avançado", "Profissional","Ismael"]
        }
            ]

resultado = prompt(perguntas)