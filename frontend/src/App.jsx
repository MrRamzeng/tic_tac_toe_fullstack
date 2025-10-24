import { useState, useEffect } from "react"
import axios from "axios"
import "./App.css"

const API_URL = "http://localhost:8000/api/game/"

function App() {
  const [game, setGame] = useState(null)
  const [loading, setLoading] = useState(false)

  const createGame = async () => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}create/`)
      setGame(response.data)
    } catch (error) {
      console.error("Create game error:", error)
    } finally {
      setLoading(false)
    }
  }

  const makeMove = async (position) => {
    if (!game || game.winner || game.board[position]) return
    try {
      const response = await axios.post(`${API_URL}${game.id}/move/`, {position: position})
      setGame(response.data)
    } catch (error) {
      console.error("Make move error:", e)
    }
  }

  useEffect(() => {
    createGame()
  }, [])

  const renderCell = (value, index) => (
    <button
      key={index}
      onClick={() => makeMove(index)}
      className="w-20 h-20 border text-3xs font-bold"
    >
      {value}
    </button>
  )

  if (!game) return <div className="p-4">Loading...</div>

  return (
    <div className="flex flex-col items-center justify-center gap-4 p-4">
      <h1 className="text-2xl font-bold">tic tac toe</h1>

      <div className="grid grid-cols-3 gap-1">
        {game.board.map((cell, index) => renderCell(cell, index))}
      </div>

      <div className="text-lg">
        {game.winner
          ? game.winner === "D"
            ? "D"
            : `win ${game.winner}`
          : `Move ${game.current_player}`
        }
      </div>
      <button
        onClick={createGame}
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-2"
      >
        New game
      </button>
    </div>
  )
}

export default App
