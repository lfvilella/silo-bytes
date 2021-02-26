import React, { useEffect } from 'react';
import { Container, LoadingIcon } from './styles';
import AsyncStorage from '@react-native-community/async-storage';
import { useNavigation } from '@react-navigation/native';

import { UserContext } from '../../contexts/UserContext';

import Api from '../../Api';

import SiloLogo from '../../assets/silo.svg';

export default () => {
    const navigation = useNavigation();

    useEffect(() => {
        const checkToken = async () => {
            const token = await AsyncStorage.getItem('token');
            if (token) {
                let response = await Api.checkToken(token);
                if (response.token) {
                    await AsyncStorage.setItem('token', response.token);

                    navigation.reset({
                        routes: [{ name: 'Home' }]
                    });
                }
                else {
                    navigation.navigate('SignIn');
                }
            }
            else {
                navigation.navigate('SignIn');
            }
        }

        checkToken();
    }, []);

    return (
        <Container>
            <SiloLogo width="100%" height="230" />
            <LoadingIcon size="large" color="#FFFFFF" />
        </Container>
    );
}
