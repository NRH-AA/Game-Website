import { useState, useEffect, useCallback } from 'react';
import './index.css'

const AllPlayersComponent = () => {
    const [players, setPlayers] = useState(null);
    
    const getAllPlayers = useCallback(async () => {
        const res = fetch('/api/player', { method: 'GET'});
        
        if (res.ok) {
            const data = await res.json();
            setPlayers(data)
        }
    }, [])
    
    useEffect(() => {
        if (!players) getAllPlayers();
    }, [getAllPlayers, players])
    
    return (
        <div id='all-players-container'>
            {players?.map((player, i) => 
                <div key={i} className='player-container'>
                    <p>{player.name}</p>
                </div>
            )}
            
            {!players?.length && <h2>No player data</h2>}
        </div>
    );
};

export default AllPlayersComponent;
