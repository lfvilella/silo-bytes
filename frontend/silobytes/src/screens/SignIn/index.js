import React, { useState, useContext } from 'react';
import { useNavigation } from '@react-navigation/native';
import AsyncStorage from '@react-native-community/async-storage';

import { UserContext } from '../../contexts/UserContext';

import {
    Container,
    InputArea,
    CustomButton,
    CustomButtonText,
} from './styles';

import Api from '../../Api';

import SignInput from '../../components/SignInput';

import SiloLogo from '../../assets/silo.svg';
import UserIcon from '../../assets/user_icon.svg';
import LockIcon from '../../assets/lock_icon.svg';

export default () => {
    const { dispatch: userDispatch } = useContext(UserContext);
    const navigation = useNavigation();

    const [usernameField, setUsernameField] = useState('');
    const [passwordField, setPasswordField] = useState('');

    const handleSignClick = async () => {
        if (usernameField !== '' && passwordField !== '') {
            let json = await Api.signIn(usernameField, passwordField);
            if (json.token) {
                await AsyncStorage.setItem('token', `Token ${json.token}`);

                // userDispatch({
                //     type: 'setAvatar',
                //     payload: {
                //         avatar: json.data.avatar
                //     }
                // });

                navigation.reset({
                    routes: [{ name: 'Home' }]
                });
            }
            else {
                alert('Username e/ou senha errado(s) !')
            }
        }
        else {
            alert('Preencha os campos!')
        }
    }

    return (
        <Container>
            <SiloLogo width="100%" height="230" />

            <InputArea>
                <SignInput
                    IconSvg={UserIcon}
                    placeholder="Digite seu email"
                    value={usernameField}
                    onChangeText={text => setUsernameField(text)}
                />
                <SignInput
                    IconSvg={LockIcon}
                    placeholder="Digite sua senha"
                    value={passwordField}
                    onChangeText={text => setPasswordField(text)}
                    password={true}
                />

                <CustomButton onPress={handleSignClick}>
                    <CustomButtonText>LOGIN</CustomButtonText>
                </CustomButton>
            </InputArea>
        </Container>
    );
}
