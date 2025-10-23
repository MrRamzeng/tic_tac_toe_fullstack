import { useState } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState("TicTacToe React");

  return (
    <div className="flex flex-col items-center justify-center min-h-screen text-xl">
      <h1>{message}</h1>
    </div>
  )
}

export default App
