import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [number, setNumber] = useState({number1:'',number2:'',sum:''})

    const onChange_call = (event)=>{
      setNumber({...number,[event.target.name]: event.target.value})
    }
  return (
      <div className="App">
          <input type="text" placeholder="enter a number" name="number1" onChange={onChange_call}/><br/>
          <input type="text" placeholder="enter a number" name="number2" onChange={onChange_call}/><br/>
          <button onClick={()=>{setNumber({...number,sum:parseInt(number.number1)+parseInt(number.number2)})}}>+</button>
          <button onClick={()=>{setNumber({...number,sum:parseInt(number.number1)-parseInt(number.number2)})}}>-</button>
          <button onClick={()=>{setNumber({...number,sum:parseInt(number.number1)*parseInt(number.number2)})}}>*</button>
          <button onClick={()=>{setNumber({...number,sum:parseInt(number.number1)/parseInt(number.number2)})}}>/</button>
          <h1>{number.sum}</h1>
      </div>
  )
}

export default App
