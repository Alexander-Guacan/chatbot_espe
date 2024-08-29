import './App.css'
import { Chatbot } from './components/chatbot'
import { NavBar } from './components/NavBar'

function App() {

  return (
    <>
      <NavBar />
      <main className='main'>
        <Chatbot />
      </main>
    </>
  )
}

export default App
