import { Link } from 'react-router-dom'
import logo from './../assets/espe.png'
import './NavBar.css'

export function NavBar() {
  const pages = [
    {
      url: "/about_us",
      text: "Acerca de"
    },
  ]

  return (
    <header className="navbar">
      <div>
        <Link className='link' to={'/'}>
          <img className='img logo' src={logo} alt="espe logo" />
        </Link>
      </div>

      <h1 className='title'>Chatbot-ESPE</h1>

      <nav>
        <ul className='menu'>
          {
            pages.map((page, index) => (
              <li key={index}>
                <Link className='link' to={page.url} >{page.text}</Link>
              </li>
            ))
          }
        </ul>
      </nav>
    </header>
  )

}