import React, { useState, useEffect } from 'react';
import { RefreshControl } from 'react-native';

import Api from '../../Api';

import {
    Container,
    Scroller,
    SearchButton,
    SearchArea,
    SearchInput,
    HeaderArea,
    HeaderTitle,
    LoadingIcon,
    ListArea,
} from './styles';

import StorageItem from '../../components/StorageItem';

import SearchIcon from '../../assets/loupe.svg'

export default () => {
    const [searchText, setSearchText] = useState('');
    const [loading, setLoading] = useState(false);
    const [list, setList] = useState([]);
    const [refreshing, setRefreshing] = useState(false);

    const listStorage = async () => {
        setLoading(true);
        setList([]);

        let response = await Api.listStorage(searchText);
        if (response.detail != 'Invalid token.') {
            setList(response);
        }
        else {
            alert('Erro: ' + response)
        }
        setLoading(false);
    }

    useEffect(() => {
        listStorage();
    }, []);

    const onRefresh = () => {
        setRefreshing(false);
        listStorage();
    }

    return (
        <Container>
            <Scroller refreshControl={
                <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
            }>
                <SearchArea>
                    <SearchInput
                        placeholder="Onde você está?"
                        placeholderTextColor="#35512B"
                        value={searchText}
                        onChangeText={text => setSearchText(text)}
                        onEndEditing={listStorage}
                    />
                    <SearchButton onPress={listStorage}>
                        <SearchIcon width="26" height="26" fill="#35512B" />
                    </SearchButton>
                </SearchArea>

                <HeaderArea>
                    <HeaderTitle>Storages</HeaderTitle>
                </HeaderArea>

                {loading &&
                    <LoadingIcon size="large" color="#FFFFFF" />
                }

                <ListArea>
                    {list.map((item, key) => (
                        <StorageItem key={key} data={item} />
                    ))}
                </ListArea>
            </Scroller>
        </Container>
    )
}
