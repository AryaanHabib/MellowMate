from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai

# Set OpenAI API key
# openai.api_key = "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"

class ChatAPIView(APIView):
    def post(self, request):
        """
        Handles user messages and generates AI responses using OpenAI API.
        """
        user_message = request.data.get('message', '').strip()  # Trim whitespace and newlines
        if not user_message:
            return Response({"error": "No message provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve or initialize chat history from the session
        chat_history = request.session.get('chat_history', [])
        chat_history.append({"role": "user", "content": user_message})

        try:
            # Generate AI response using OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *chat_history,
                ]
            )
            bot_message = response['choices'][0]['message']['content']

            # Add AI response to the chat history
            chat_history.append({"role": "assistant", "content": bot_message})
            request.session['chat_history'] = chat_history  # Save updated history in the session
            request.session.modified = True  # Ensure session is saved

            return Response({"message": bot_message}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Failed to fetch response from OpenAI: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChatHistoryAPIView(APIView):
    def get(self, request):
        chat_history = request.session.get('chat_history', [])
        return Response(chat_history, status=status.HTTP_200_OK)
