import openai

# Configura tu clave de API
openai.api_key = 'sk-98_SdhMEjp462pEUympWx9RZLLktzZzp663Bkjq_sAT3BlbkFJqoiac96FcxuEVIu8PCXNCEUoHhIOIfB6wW2r7j1VMA'

# Prueba 1
# prompt = "Eres un asistente de Python. Escribe un código para calcular la suma de los primeros 100 números."

# Realiza la llamada al modelo


# def generar_respuesta(pregunta):
#   respuesta = openai.Completion.create(
#     engine="gpt-3.5-turbo-instruct",
#     prompt=pregunta,
#     max_tokens=50
# )


#   return respuesta.choices[0].text.strip()


# def main():
#   print("Bienvenido al Chat bot de OpenAI")

#   while True:
#     pregunta = input("Escribe tu pregunta (o 'salir' para finalizar): ")

#     if pregunta.lower() == 'salir':
#       print("Hata luego!")
#       break
#     respuesta = generar_respuesta(pregunta)
#     print("Respuesta:", respuesta)

# if __name__ == "__main__":
#   main()

class CallCenterAssistant:
    def __init__(self):
        self.general_objective = ("El asistente debe ayudar al cliente a resolver problemas técnicos con su "
                                  "servicio de internet, manteniendo un tono profesional, amable y empático. "
                                  "El objetivo es resolver el problema en la primera llamada siempre que sea posible.")
        self.tone_and_style = ("Mantén un tono amable y empático en todo momento. Sé claro y conciso en tus "
        "explicaciones, y asegúrate de que el cliente se sienta escuchado y comprendido.")
        self.procedures = [
            "Verifica el estado de la cuenta del cliente al inicio de la llamada.",
            "Si el cliente está experimentando problemas de conexión, guía al cliente a través de los pasos "
            "básicos de solución de problemas, como reiniciar el módem o verificar las conexiones de los cables.",
            "Si no puedes resolver el problema de manera remota, programa una visita técnica dentro de las "
            "próximas 24-48 horas."
        ]
        self.limits_and_restrictions = ("No ofrezcas reembolsos o descuentos sin autorización previa. "
                                        "Si no estás seguro de una respuesta, deriva la consulta a un especialista.")
        self.escalation_handling = ("Si no puedes resolver el problema en la llamada, informa al cliente sobre "
                                    "la necesidad de escalar el caso y proporciona una estimación de tiempo para "
                                    "la resolución. Asegúrate de que el cliente entienda los próximos pasos.")
        self.phrases = [
            "Lamento mucho que estés experimentando este problema. Vamos a solucionarlo juntos.",
            "Permíteme revisar los detalles de tu cuenta para entender mejor la situación.",
            "Voy a programar una visita técnica para que podamos resolver este problema lo antes posible."
        ]

    def generate_response(self, customer_query):
        prompt = f"""
        Eres un asistente de soporte técnico en un call center. Tu objetivo es ayudar al cliente a resolver problemas técnicos con su servicio de internet. Mantén un tono amable y empático. Aquí está el contexto:

        - Objetivo General: {self.general_objective}
        - Tono y Estilo: {self.tone_and_style}
        - Procedimientos: {', '.join(self.procedures)}
        - Límites y Restricciones: {self.limits_and_restrictions}
        - Manejo de Escalaciones: {self.escalation_handling}

        El cliente pregunta: "{customer_query}"

        Responde de manera profesional y empática.
        """

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text.strip()

# Ejemplo
assistant = CallCenterAssistant()
customer_query = "Hola, tenngo problema con mi servicio, ¿qué puedo hacer?"
response = assistant.generate_response(customer_query)
print(response)
