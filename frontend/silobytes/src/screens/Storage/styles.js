import styled from 'styled-components/native';


export const Container = styled.SafeAreaView`
    flex: 1;
    background-color: #FFFFFF;
`;

export const PageBody = styled.View`
    background-color: #FFFFFF;
    border-top-left-radius: 50px;
    margin-top: -50px;
`;

export const BackButton = styled.TouchableOpacity`
    position: absolute;
    left: 0;
    top: 45px;
    z-index: 9;
`;

export const LoadingIcon = styled.ActivityIndicator`
    margin-top: 50px;
`;


export const FakeArea = styled.View`
    height: 140px;
    background-color: #97CE84;
`;


export const StorageInfoArea = styled.View`
    background-color: transparent;
    align-items: center;
    margin-top: 10px;
`;

export const StorageInfo = styled.View`
    background-color: transparent;
    justify-content: flex-end;
`;

export const StorageInfoName = styled.Text`
    color: #35512B;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 20px;
`;

export const Circle = styled.View`
    width: 40px;
    height: 40px;
    border-radius: 20px;
    background-color: #FD5C5C;
    border: 2px solid #FFFFFF;
    position: absolute;
    top: -25px;
    left: 150px;
`

export const CardsArea = styled.View``

export const ShortCardsArea = styled.View`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0 50px;
`

export const ShortCardsLeftColumn = styled.View`
`

export const ShortCardsRightColumn = styled.View`
`

export const ShortCardItem = styled.View`
    align-items: center;
`

export const CardsLabel = styled.Text`
    font-size: 16px;
    color: #35512B;
    margin-bottom: 2px;
`

export const ShortCard = styled.View`
    background-color: #97CE84;
    border-radius: 5px;
    width: 150px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
`

export const CardText = styled.Text`
    font-size: 25px;
    font-weight: bold;
    color: #FFFFFF;
`

export const LongCardsArea = styled.View``;

export const LongCardItem = styled.View`
    align-items: center;
`;

export const LongCard = styled.View`
    background-color: #97CE84;
    border-radius: 5px;
    width: 210px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
`;

export const AnotationsArea = styled.View`
    margin: 10px 0px;
    padding: 0px 20px;
    align-items: center;
`

export const AnotationsLabel = styled.Text`
    align-self: flex-start;
    color: #35512B;
    font-size: 22px;
    font-weight: bold;
    margin-left: 25px;
`

export const AnotationItem = styled.View`
    background-color: #D5F0DB;
    border-radius: 5px;
    width: 360px;
    height: 120px;
    padding: 5px 20px;
`

export const AnotationsText = styled.Text`
    font-size: 18px;
`

export const ButtonWithdrawArea = styled.TouchableOpacity`
    margin-top: 10px;
    align-self: center;
    width: 360px;
    height: 50px;
    background-color: #97CE84;
    border-radius: 30px;
    align-items: center;
    justify-content: center;
`

export const ButtonWithdrawText = styled.Text`
    color: #FFFFFF;
    font-size: 25px;
    font-weight: bold;
`
