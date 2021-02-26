import AsyncStorage from '@react-native-community/async-storage';

const BASE_API = 'http://localhost:8002/api';


export default {
    checkToken: async (token) => {
        const request = await fetch(`${BASE_API}/auth/verify/`, {
            method: 'GET',
            headers: new Headers({
                'Content-Type': 'application/json',
                'Authorization': token,
            }),
        });
        const json = await request.json();
        return json;
    },
    signIn: async (username, password) => {
        const request = await fetch(`${BASE_API}/auth/login/`, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        const json = await request.json();
        return json;
    },
    listStorage: async (value = null) => {
        const token = await AsyncStorage.getItem('token');

        let url = `${BASE_API}/storages/`;
        if (value) {
            url = url + `?search=${value}`
        }

        const request = await fetch(url, {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': token,
            },
        });
        const json = await request.json();
        return json;
    },
    getStorage: async (id) => {
        const token = await AsyncStorage.getItem('token');

        const request = await fetch(`${BASE_API}/storages/${id}/`, {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': token,
            },
        });

        const json = await request.json();
        return json;
    },
    updateStorageWithdrawToNow: async (id) => {
        const token = await AsyncStorage.getItem('token');

        const request = await fetch(`${BASE_API}/storages/${id}/withdraw-now/`, {
            method: 'PATCH',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': token,
            },
        });

        const json = await request.json();
        return json;
    },
};
