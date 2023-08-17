
const APIURL = 'http://127.0.0.1:3000/api_v1/';
//const APIURL = 'https://espndraftboard.com/api/';

function getCurrentYear() {
    const currentDate = new Date();
    return currentDate.getFullYear();
}

export async function fetchDraft(id) {
    try {
        const response = await fetch(`${APIURL}get-draft/${id}-${getCurrentYear()}/`, {
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching draft:', error.message);
    }
}

export async function fetchTeams(id) {
    try {
        const response = await fetch(`${APIURL}get-teams/${id}-${getCurrentYear()}/`, {
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching teams:', error.message);
    }
}

export async function fetchPicks(id) {
    try {
        const response = await fetch(`${APIURL}get-picks/${id}-${getCurrentYear()}/`, {
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching picks:', error.message);
    }
}

export async function fetchTimer(id) {
    try {
        const response = await fetch(`${APIURL}get-timer/${id}-${getCurrentYear()}/`, {
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching timer:', error.message);
    }
}


