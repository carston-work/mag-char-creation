function allowDrop(ev) {
    ev.preventDefault(); 
}
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    if (ev.target.id === 'powers') {
        document.getElementById('pasHelpText').textContent = `If you set your characters Powers to strong, you will play as a Mistborn, with access to all 16 Allomantic powers, or as a Keeper with all 16 Feruchemical powers.
        By setting them to average, you can play as a Misting, with access to just 1 Allomantic power, or as a kandra with the power of Mimicry AKA shapeshifting.
        If you set Powers to weak, then your character will have no powers.`
    } else if (ev.target.id === "attributes") {
        document.getElementById('pasHelpText').textContent = `Attributes are your character's internal stats: Physique, Charm, and Wits. Physique helps you overcome physical obstacles, Charm can be used to influence others and bluff your way to victory, and Wits defines your characters ability to reason through situations and come up with the winning solution.`
    } else if (ev.target.id === 'standings') {
        document.getElementById('pasHelpText').textContent = `Standings are your character's external stats: Resources, Influence, and Spirit. Resources: Wealth, privilege, and capacity to muster financially-driven
        resources (like raising an army or running an estate). Infl uence: Political power, contacts, and ability to call in favors. Spirit: Fate, connection to the metaphysical, and ability to survive against
        the odds`
    }
}

const allAtts = document.querySelectorAll(".atts")
const allStands = document.querySelectorAll(".stands")
let powersStrength = ''
let attsStrength = 0
let standsStrength = 0
let health = 4
let reputation = 4
let willpower = 4

function speciesCheck() {
    const speciesWarning = document.getElementById('speciesWarning')
    const strengthsList = document.getElementById('strengthsList')
    if (strengthsList.children.item(0).firstElementChild.textContent === 'Powers') {
        speciesWarning.textContent = 'You can play as a noble, skaa, or Terris character'
        powersStrength = 'strong'
    } else if (strengthsList.children.item(1).firstElementChild.textContent === 'Powers') {
        speciesWarning.textContent = 'You can play as a noble, skaa, or kandra character'
        powersStrength = 'average'
    } else if (strengthsList.children.item(2).firstElementChild.textContent === 'Powers') {
        speciesWarning.textContent = 'You can play as a noble, skaa, or Terris character'
        powersStrength = 'weak'
    } else {
        speciesWarning.textContent = ""
        powersStrength = ''
    }
    updatePowers()
    updateRace()
}

function drop(ev) {
    ev.preventDefault();
    if (ev.target.classList.contains('strengthsBoxes') && ev.target.children.length < 1) {
        var data = ev.dataTransfer.getData("text");
        ev.target.appendChild(document.getElementById(data));
        const sourceList = document.querySelector('.emptyBoxes').firstElementChild
        for (let i = 0; i < sourceList.children.length; i++) {
            if (!sourceList.children[i].firstElementChild) {
                sourceList.children[i].remove()
            }
        }
        attriCheck()
        standCheck()
        let nums = document.querySelectorAll(".nums")
        if (sourceList.children.length === 0) {
            nums.forEach(elem => elem.readOnly = false)
        } else {
            nums.forEach(elem => elem.readOnly = true)
        }
        updateHealth()
        updateRep()
        updateWill()
        speciesCheck()
    }
}

function unselectedDrop(ev) {
    ev.preventDefault();
    if (ev.target.classList.contains('emptyBoxes')) {
        const listItem = document.createElement('li')
        const draggedId = ev.dataTransfer.getData("text")
        listItem.appendChild(document.getElementById(draggedId))
        ev.target.firstElementChild.appendChild(listItem)
        const sourceList = document.querySelector('.emptyBoxes').firstElementChild
        for (let i = 0; i < sourceList.children.length; i++) {
            if (!sourceList.children[i].firstElementChild) {
                sourceList.children[i].remove()
            }
        }
        attriCheck()
        standCheck()
        let nums = document.querySelectorAll(".nums")
        if (sourceList.children.length === 0) {
            console.log('readyonly false')
            nums.forEach(elem => elem.readOnly = false)
        } else {
            console.log('reaodnly true')
            nums.forEach(elem => elem.readOnly = true)
        }
        updateHealth()
        updateRep()
        updateWill()
        speciesCheck()
    }
}

function attriCheck() {
    console.log("is this running?")
    const atts = document.getElementById('attPts')
    const strengthsList = document.getElementById('strengthsList')
    if (strengthsList.children.item(0).firstElementChild.textContent === 'Attributes') {
        atts.textContent = '7'
        attsStrength = 13
    } else if (strengthsList.children.item(1).firstElementChild.textContent === 'Attributes') {
        atts.textContent = '5'
        attsStrength = 11
    } else if (strengthsList.children.item(2).firstElementChild.textContent === 'Attributes') {
        atts.textContent = '3'
        attsStrength = 9
    } else {
        atts.textContent = ''
        attsStrength = 0
    }
    for (let i = 0; i < allAtts.length; i++) {
        allAtts[i].value = '2'
    }
}

function standCheck() {
    const stands = document.getElementById('standPts')
    const strengthsList = document.getElementById('strengthsList')
    if (strengthsList.children.item(0).firstElementChild.textContent === 'Standings') {
        stands.textContent = '7'
        standsStrength = 13
    } else if (strengthsList.children.item(1).firstElementChild.textContent === 'Standings') {
        stands.textContent = '5'
        standsStrength = 11
    } else if (strengthsList.children.item(2).firstElementChild.textContent === 'Standings') {
        stands.textContent = '3'
        standsStrength = 9
    } else {
        stands.textContent = ''
        standsStrength = 0
    }
    for (let i = 0; i < allStands.length; i++) {
        allStands[i].value = '2'
    }
}

for (let i = 0; i < allStands.length; i++) {
    allStands[i].addEventListener('change', () => {

        total = 0
        for (let j = 0; j < allStands.length; j++) {
            total += parseInt(allStands[j].value)
        }
        const stands = document.getElementById('standPts')
        stands.textContent = standsStrength - total
        if (parseInt(stands.textContent) === 0) {
            for (let j = 0; j < allStands.length; j++) {
                allStands[j].max = allStands[j].value
            }
        } else {
            for (let j = 0; j < allStands.length; j++) {
                allStands[j].max = standsStrength
            }
        }
        updateHealth()
        updateRep()
        updateWill()
    })
}

for (let i = 0; i < allAtts.length; i++) {
    allAtts[i].addEventListener('change', () => {

        total = 0
        for (let j = 0; j < allAtts.length; j++) {
            total += parseInt(allAtts[j].value)
        }
        const atts = document.getElementById('attPts')
        atts.textContent = attsStrength - total
        if (parseInt(atts.textContent) <= 0) {
            for (let j = 0; j < allAtts.length; j++) {
                allAtts[j].max = allAtts[j].value
            }
        } else {
            for (let j = 0; j < allAtts.length; j++) {
                allAtts[j].max = attsStrength
            }
        }
        updateHealth()
        updateRep()
        updateWill()
    })
}

function updateHealth() {
    const phys = document.querySelectorAll(".physical");
    let sum = 0
    phys.forEach(elem => sum += parseInt(elem.value))
    health = sum
    document.getElementById('health').textContent = health
}

function updateRep() {
    const cogs = document.querySelectorAll(".cognitive");
    let sum = 0
    cogs.forEach(elem => sum += parseInt(elem.value))
    reputation = sum
    document.getElementById('reputation').textContent = reputation
}

function updateWill() {
    const spirit = document.querySelectorAll(".spiritual");
    let sum = 0
    spirit.forEach(elem => sum += parseInt(elem.value))
    willpower = sum
    document.getElementById('willpower').textContent = willpower
}

function updatePowers() {
    const powerButs = document.querySelectorAll(".powers")
    powerButs.forEach(elem => {
        elem.checked = false
        if (elem.classList.contains(powersStrength)) {
            elem.style.visibility = "visible"
        } else {
            elem.style.visibility = "hidden"
        }
    })
}

function updateRace() {
    const raceButs = document.querySelectorAll(".race")
    const powerButs = document.querySelectorAll(".powers")
    raceButs.forEach(elem => {
        elem.checked = false
        if (document.querySelector('input[name="powers"]:checked')) {
            if (elem.classList.contains(document.querySelector('input[name="powers"]:checked').value)) {
                elem.style.visibility = "visible"
            } else {
                elem.style.visibility = "hidden"
            }
        } else {
            elem.style.visibility = "hidden"
        }
    })
}

document.querySelectorAll('.powers').forEach(elem => {
    elem.addEventListener('change', updateRace)
})

class Character {
    constructor(details, atts, stands, traits, tragedy, destiny, powers, equipment, backstory) {
        this.details = details
        this.atts = atts
        this.stands = stands
        this.traits = traits
        this.tragedy = tragedy
        this.destiny = destiny
        this.powers = powers
        this.equipment = equipment
        this.backstory = backstory
    }
}   

function createCharacter() {
    const details = {
        name: document.getElementById('charName').value,
        concept: document.getElementById('concept').value,
        crew: document.getElementById('crewName').value,
        cause: document.getElementById('cause').value,
        target: document.getElementById('target').value,
        method: document.getElementById('method').value,
        race: document.querySelector('input[name="races"]:checked').value,
        sex: document.getElementById('gender').value,
        age: document.getElementById('age').value,
        height: document.getElementById('height').value,
        weight: document.getElementById('weight').value
    }

    const atts = {
        physique: document.getElementById('physique').value,
        charm: document.getElementById('charm').value,
        wits: document.getElementById('wits').value
    }

    const stands = {
        resources: document.getElementById('resources').value,
        influence: document.getElementById('influence').value,
        spirit: document.getElementById('spirit').value
    }

    const traits = []
    document.querySelectorAll('.traits').forEach(elem => {
        traits.push(elem.value)
    })

    const tragedy = document.getElementById('tragedy').value

    const destiny = document.getElementById('destiny').value

    const powers = document.querySelector('input[name="powers"]:checked').value

    const equipment = []
    document.querySelectorAll('input[name="props"]:checked').forEach(elem => {
        console.log('euipment')
        equipment.push(elem.id)
    })

    const backstory = document.getElementById('backstory').value

    const newChar = new Character(details, atts, stands, traits, tragedy, destiny, powers, equipment, backstory)

    axios.post('http://localhost:4000/newChar', newChar) 
        .then( res => {
            window.location.href = res.data
        })
}

document.getElementById('submit').addEventListener('click', createCharacter)

let wallet = 0

document.getElementById('resources').addEventListener('change', () => {
    document.querySelectorAll('.props').forEach(elem => {
        elem.selected = false
    });
    document.getElementById('wallet').textContent = document.getElementById('resources').value
    wallet = parseInt(document.getElementById('resources').value)
})

document.querySelectorAll(".props").forEach(elem => {
    elem.addEventListener('change', () => {
    const allProps = document.querySelectorAll('input[name="props"]:checked')
    let sum = 0
    for (let i = 0; i < allProps.length; i++) {
        sum += parseInt(allProps[i].value)
    }
    document.getElementById('wallet').textContent = wallet - sum
    const realAllProps = document.querySelectorAll('input[name="props"]')
    // const forRealAllProps = []
    // for (let i = 0; i < allProps.length; i++) {
    //     for (let j = 0; j < realAllProps.length; j++) {
    //         if (allProps[i] === realAllProps[j]) {
    //             forRealAllProps.push(realAllProps[j])
    //             break
    //         }
    //     }
    // }
    if (parseInt(document.getElementById('wallet').textContent) < 1) {
        //everything blackedout
        realAllProps.forEach(elem => {
            if (!elem.checked) {
                elem.disabled = true 
            }
        })
    } else if (parseInt(document.getElementById('wallet').textContent) < 2) {
        //only big ones blacked out
        realAllProps.forEach(elem => {
            if (!elem.checked) {
                if (elem.value === "2") {
                    elem.disabled = true
                } else {
                    elem.disabled = false
                }
            }
        })
    } else {
        //everything blacked in
        document.querySelectorAll('input[name="props"]').forEach(elem => {
            elem.disabled = false
        })
    }
    });
});