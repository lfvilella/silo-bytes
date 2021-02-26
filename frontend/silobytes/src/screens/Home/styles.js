import styled from 'styled-components/native';

export const Container = styled.SafeAreaView`
    flex: 1;
    background-color: #97CE84;
`;

export const Scroller = styled.ScrollView`
    flex: 1;
    padding: 20px;
`;

export const SearchButton = styled.TouchableOpacity`
    width: 26px;
    height: 26px;
`;

export const SearchArea = styled.View`
    background-color: #F1FFF4;
    height: 60px;
    border-radius: 30px;
    flex-direction: row;
    align-items: center;
    padding-left: 20px;
    padding-right: 20px;
`;

export const SearchInput = styled.TextInput`
    flex: 1;
    font-size: 16px;
    color: #35512B;
`;

export const HeaderArea = styled.View`
    margin-top: 24px;
`;

export const HeaderTitle = styled.Text`
    font-size: 40px;
    font-weight: bold;
    color: #F1FFF4;
`;

export const LoadingIcon = styled.ActivityIndicator`
    margin-top: 50px;
`;

export const ListArea = styled.View`
    margin-top: 10px;
    margin-bottom: 30px;
`;
