axios.get('/getChar/0')
    .then(res => {
        const { details, atts, stands, traits, tragedy, destiny, powers, equipment, backstory } = res.data
        for (detail in details) {
            document.getElementById(detail).textContent = details[detail]
        }
        // document.getElementById('name').textContent = details.name
        // document.getElementById('concept').textContent = details.concept
        // document.getElementById('crew').textContent = details.crew
        // document.getElementById('cause').textContent = details.cause
        // document.getElementById('target').textContent = details.target
        // document.getElementById('method').textContent = details.method
        // document.getElementById('race').textContent = details.race
        // document.getElementById('sex').textContent = details.sex
        // document.getElementById('age').textContent = details.age
        // document.getElementById('height').textContent = details.height
        // document.getElementById('weight').textContent = details.weight
        for (let att in atts) {
            document.getElementById(att).textContent = atts[att]
        }
        for (let stand in stands) {
            document.getElementById(stand).textContent = stands[stand]
        }
        for (let trait of traits) {
            const newTrait = document.createElement('p')
            newTrait.textContent = trait
            document.getElementById('traits').appendChild(newTrait)
        }
        const tragedia = document.createElement('p')
        tragedia.textContent = tragedy
        document.getElementById('tragedy').appendChild(tragedia)
        const destino = document.createElement('p')
        destino.textContent = destiny
        document.getElementById('destiny').appendChild(destino)
        const pow = document.createElement('p')
        pow.textContent = powers
        document.getElementById('powers').appendChild(pow)
        for (let item of equipment) {
            const newEquip = document.createElement('p')
            newEquip.textContent = item
            document.getElementById('equipment').appendChild(newEquip)
        }
        const back = document.createElement('p')
        back.textContent = backstory
        document.getElementById('backstorydiv').appendChild(back)
        document.getElementById('health').textContent = parseInt(atts.physique) + parseInt(stands.resources)
        document.getElementById('reputation').textContent = parseInt(atts.charm) + parseInt(stands.influence)
        document.getElementById('willpower').textContent = parseInt(atts.wits) + parseInt(stands.spirit)
        axios.delete('/delete').then(res=> {})
    })