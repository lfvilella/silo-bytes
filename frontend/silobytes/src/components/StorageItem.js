import React from 'react';
import styled from 'styled-components/native';
import { useNavigation } from '@react-navigation/native'


const Area = styled.TouchableOpacity`
    background-color: #FFFFFF;
    margin-bottom: 20px;
    border-radius: 20px;
    padding: 15px;
    flex-direction: row;
    justify-content: space-between;
`;

const LeftArea = styled.View`
    margin-left: 10px;
    justify-content: space-between;
`;

const RightArea = styled.View`
    margin-right: 10px;
    justify-content: flex-end;
    align-items: center;
`;

const SiloName = styled.Text`
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 10px;
`;

const ClientText = styled.Text`
    font-size: 15px;
`;

const ProductText = styled.Text`
    font-size: 15px;
`;


const Circle = styled.View`
    width: 40px;
    height: 40px;
    border-radius: 20px;
    background-color: #FD5C5C;
    border: 2px solid #FFFFFF;
    position: absolute;
    top: -25px;
    right: 5px;
`

const DateText = styled.Text`
    font-size: 12px;
    margin-bottom: 5px;
`;

const SeeStorageButton = styled.View`
    width: 160px;
    height: 26px;
    border: 1px solid #35512B;
    border-radius: 10px;
    justify-content: center;
    align-items: center;
`;

const SeeStorageButtonText = styled.Text`
    font-size: 13px;
    color: #35512B
`;


export default ({ data }) => {
    const navigation = useNavigation();

    const handleClick = () => {
        navigation.navigate('Storage', {
            id: data.id,
            siloName: data.silo.name,
            currentStatus: data.current_status,
        });
    }

    return (
        <Area onPress={handleClick}>
            <LeftArea>
                <SiloName>{data.silo.name}</SiloName>
                <ClientText>Client: {data.client.name}</ClientText>
                <ProductText>Product: {data.product.name}</ProductText>
            </LeftArea>

            <RightArea>
                {data.current_status === 'occupied' &&
                    <Circle />
                }
                {data.current_status === 'scheduled' &&
                    <Circle style={{ backgroundColor: '#FFD064' }} />
                }
                {data.current_status === 'disabled' &&
                    <Circle style={{ backgroundColor: '#B8B6B6' }} />
                }
                <DateText>{data.entry_date.slice(0, 10)} - {data.withdrawal_date.slice(0, 10)}</DateText>
                <SeeStorageButton>
                    <SeeStorageButtonText>Details</SeeStorageButtonText>
                </SeeStorageButton>
            </RightArea>
        </Area>
    );
}
