import { useEffect, useState } from 'react'
import MemeCard from './MemeCard'
import MemeForm from './MemeForm'

function MemesContainer() {

    const URL = "/api/memes"
    const [memes, setMemes] = useState([])

    useEffect(() => {
        fetch(URL)
        .then(res => res.json())
        .then(data => setMemes(data) )
        .catch(error => alert(error))
    }, [])

    const mappedCards = memes.map(m => <MemeCard key={m.id} meme={m} />)

    return (
        <div>

            <MemeForm setMemes={setMemes} />

            { mappedCards }

        </div>
    )

}

export default MemesContainer