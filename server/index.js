const express = require('express')
const cors = require('cors')
const path = require('path')

const app = express()
app.use(express.json())
app.use(cors())

const characters = [] 
let charId = 0

app.get('/viewChar', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/viewChar.html'))
})

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/newCharacter.html'))
})

app.get('/style', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/newCharacterStyles.css'))
})

app.get('/viewCharScript', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/viewChar.js'))
})
app.get('/newCharacterScript', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/newCharacter.js'))
})

app.post('/newChar', (req, res) => {
    const { details, atts, stands, traits, tragedy, destiny, powers, equipment, backstory } = req.body;
    const newChar = {id: charId, details, atts, stands, traits, tragedy, destiny, powers, equipment, backstory }
    charId++
    characters.push(newChar)
    console.log(characters)
    res.status(200).send('/viewChar')
})

app.get('/getChar/:id', (req, res) => {
    const chosenChar = characters[req.params.id]
    const sendChar = {...chosenChar}
    delete sendChar.id
    res.status(200).send(sendChar)
})

app.delete('/delete', (req, res) => {
    characters = []
    res.status(200)
})

const port = process.env.PORT || 4000


app.listen(port, () => {
    console.log(`running on port ${port}`)
})