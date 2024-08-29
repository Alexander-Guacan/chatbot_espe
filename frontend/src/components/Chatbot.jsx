import { useEffect, useRef, useState } from 'react'
import { askToChatbot } from '../services/chatbot.service'
import './Chatbot.css'
import { MessageBox } from './MessageBox'

export function Chatbot() {
  const [messages, setMessages] = useState(['Hola, ¿cuál es tu duda?'])
  let chatEnd = useRef('')

  useEffect(() => {
    chatEnd.current.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const addMessage = (message) => {
    setMessages((previousMessages) => [...previousMessages, message])
  }

  const updateChatbotAnswer = (answer) => {
    setMessages((currentMessages) => [...currentMessages.slice(0, -1), answer])
  }

  const addChatbotAnswer = async (question) => {
    let answer = "Verificando..."
    addMessage(answer)

    answer = await askToChatbot(question)
    updateChatbotAnswer(answer)
  }

  const handleSubmit = async (event) => {
    event.preventDefault()

    let { question } = Object.fromEntries(new FormData(event.target))
    question = question.trim()

    if (!question.length)
      return

    addMessage(question)
    addChatbotAnswer(question)

    event.target.reset()
  }

  return (
    <section className='chat'>
      <article className='list-viewer'>
        <div className='chat__messages'>
          {
            messages.map((message, index) => (
              <MessageBox key={index}>{message}</MessageBox>
            ))
          }
          <i ref={chatEnd}></i>
        </div>
      </article>
      <form className='chat__form' onSubmit={handleSubmit} >
        <input type='text' className='chat__question' placeholder='Pregunta...' name="question" id="question" autoFocus />
        <button className='button-icon' type='submit'>
          <img className='icon' src="https://static-00.iconduck.com/assets.00/send-icon-256x249-hgri4e1y.png" alt="send whatsapp icon" />
        </button>
      </form>
    </section>
  )
}