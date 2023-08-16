
const APIURL = 'http://localhost:3000/api_v1/';
//const APIURL = 'https://espndraftboard.com/api/';

function getCurrentYear() {
    const currentDate = new Date();
    return currentDate.getFullYear();
}

export async function fetchDraft(id, authToken) {
    try {
        const response = await fetch(`${APIURL}get-draft/${id}-${getCurrentYear()}`, {
            headers: {
                Authorization: `Bearer ${authToken}`
            }
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching draft:', error.message);
    }
}

export async function fetchTeams(id, authToken) {
    try {
        const response = await fetch(`${APIURL}get-teams/${id}-${getCurrentYear()}`, {
            headers: {
                Authorization: `Bearer ${authToken}`
            }
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching teams:', error.message);
    }
}

export async function fetchPicks(id, authToken) {
    try {
        const response = await fetch(`${APIURL}get-picks/${id}-${getCurrentYear()}`, {
            headers: {
                Authorization: `Bearer ${authToken}`
            }
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching picks:', error.message);
    }
}

export async function fetchTimer(id, authToken) {
    try {
        const response = await fetch(`${APIURL}get-timer/${id}-${getCurrentYear()}`, {
            headers: {
                Authorization: `Bearer ${authToken}`
            }
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching timer:', error.message);
    }
}


