import React, { useState } from 'react';

function BotaoContador(props) {
    const {title} = props;
    const [contador, setContador] = useState(0);
  
    const aumentarContador = () => {
      setContador(contador + 1);
    };
  
    const diminuirContador = () => {
      setContador(contador - 1);
    };
  
    return (
      <div>
        <h1>{title}: {contador}</h1>
        <button onClick={aumentarContador}>Aumentar</button>
        <button onClick={diminuirContador}>Diminuir</button>
      </div>
    );
  }
  export default BotaoContador;