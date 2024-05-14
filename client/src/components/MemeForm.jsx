import { useState } from 'react'

function MemeForm({ setMemes }) {

    const URL = '/api/memes'
    const [img_url, setImgURL] = useState("")
    const [caption, setCaption] = useState("")

    async function handleSubmit(e) {
        e.preventDefault()
        
        const options = {
            method: "POST",
            headers: { "Content-Type": "application/json", "Accept": "application/json" },
            body: JSON.stringify({ img_url, caption })
        }

        const res = await fetch(URL, options)

        if (res.ok) {
            const data = await res.json()
            setMemes(prevMemes => [...prevMemes, data])
        } else {
            alert(`${res.status}: Something went wrong`)
        }
    }

    return (
        <form onSubmit={handleSubmit}>

            <label htmlFor="img_url">Image URL:</label>

            <input name="img_url" type="text" 
            onChange={e => setImgURL(e.target.value)} 
            value={img_url} />

            <label htmlFor="caption">Caption:</label>

            <input name="caption" type="text" 
            onChange={e => setCaption(e.target.value)} 
            value={caption} />

            <input type="submit" value="Add Meme" />

        </form>
    )

}

export default MemeForm