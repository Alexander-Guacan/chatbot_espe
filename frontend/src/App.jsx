import './App.css'
import { NavBar } from './components/NavBar'
import { Route, Routes } from 'react-router-dom'
import { Home } from './pages/Home'
import { AboutUs } from './pages/AboutUs'

function App() {

  return (
    <>
      <NavBar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about_us' element={<AboutUs />} />
      </Routes>
    </>
  )
}

export default App
