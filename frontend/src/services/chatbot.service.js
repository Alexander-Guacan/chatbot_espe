export const askToChatbot = async (question) => {
  if (!question.length)
    return "No puedo responder a esa pregunta"

  const chatbotEndpoint = `${import.meta.env.VITE_API_ADDRESS}/chatbot`
  const bodyRequest = {
    "question": question
  }

  const { answer } = await fetch(chatbotEndpoint, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(bodyRequest)
  }).then(response => response.json()).catch(() => {
    return "No puedo responder a esa pregunta 😓"
  })

  return answer
}