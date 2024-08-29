import PropTypes from 'prop-types'

export function MessageBox({ children }) {
  return (
    <div><i className='message'>{children}</i></div>
  )
}

MessageBox.propTypes = {
  children: PropTypes.string.isRequired
}