import React, { component } from "react"

export default function App(props){

    return(
        <h1>Testing React Code</h1>
    )
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);