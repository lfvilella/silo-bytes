import React, { useState, useEffect } from 'react';
import { useNavigation, useRoute } from '@react-navigation/native'

import BackIcon from '../../assets/back.svg';

import {
    Container,
    Scroller,
    PageBody,
    BackButton,
    LoadingIcon,

    FakeArea,

    StorageInfoArea,
    StorageInfo,
    StorageInfoName,
    Circle,

    CardsArea,
    ShortCardsArea,
    ShortCardsLeftColumn,
    ShortCardsRightColumn,
    ShortCardItem,
    CardsLabel,
    ShortCard,
    CardText,
    LongCardsArea,
    LongCardItem,
    LongCard,

    AnotationsArea,
    AnotationsLabel,
    AnotationItem,
    AnotationsText,

    ButtonWithdrawArea,
    ButtonWithdrawText,
} from './styles';

import Api from '../../Api';


export default () => {
    const navigation = useNavigation();
    const route = useRoute();

    const [storageInfo, setStorageInfo] = useState({
        id: route.params.id,
        siloName: route.params.siloName,
        current_status: route.params.currentStatus,
    });

    const [loading, setLoading] = useState(false);

    const getStorage = async () => {
        setLoading(true);
        let response = await Api.getStorage(storageInfo.id);
        if (response.detail != 'Invalid token.' && !response.error) {
            setStorageInfo(response);
        }
        else if (response.detail == 'Invalid token.') {
            navigation.navigate('SignIn');
            alert('Erro: ' + response.detail);
        }
        else {
            alert('Erro: ' + response.detail || response.detail);
        }
        setLoading(false);
    }

    useEffect(() => {
        getStorage();
    }, []);

    const handleBackButton = () => {
        navigation.goBack();
    }

    const handleButtonClick = async () => {
        let response = await Api.updateStorageWithdrawToNow(storageInfo.id);
        if (response.error) {
            alert('Erro: ' + response.error);
        }
        else {
            getStorage();
        }
    }

    return (
        <Container>
            <FakeArea />
            <PageBody>
                <StorageInfoArea>
                    <StorageInfo>
                        <StorageInfoName>{storageInfo.siloName || storageInfo.silo.name}</StorageInfoName>
                        {storageInfo.current_status === 'occupied' &&
                            <Circle />
                        }
                        {storageInfo.current_status === 'scheduled' &&
                            <Circle style={{ backgroundColor: '#FFD064' }} />
                        }
                        {storageInfo.current_status === 'disabled' &&
                            <Circle style={{ backgroundColor: '#B8B6B6' }} />
                        }
                    </StorageInfo>
                </StorageInfoArea>

                {loading &&
                    <LoadingIcon size="large" color="#000000" />
                }

                {storageInfo.client &&
                    <CardsArea>
                        <ShortCardsArea>
                            <ShortCardsLeftColumn>
                                <ShortCardItem>
                                    <CardsLabel>Current Cost</CardsLabel>
                                    <ShortCard>
                                        <CardText>{storageInfo.current_cost}</CardText>
                                    </ShortCard>
                                </ShortCardItem>

                                <ShortCardItem>
                                    <CardsLabel>Client</CardsLabel>
                                    <ShortCard>
                                        <CardText>{storageInfo.client.name}</CardText>
                                    </ShortCard>
                                </ShortCardItem>

                                <ShortCardItem>
                                    <CardsLabel>Quantity (T)</CardsLabel>
                                    <ShortCard>
                                        <CardText>{storageInfo.quantity}</CardText>
                                    </ShortCard>
                                </ShortCardItem>
                            </ShortCardsLeftColumn>

                            <ShortCardsRightColumn>
                                <ShortCardItem>
                                    <CardsLabel>Total Cost</CardsLabel>
                                    <ShortCard>
                                        <CardText>{storageInfo.total_cost}</CardText>
                                    </ShortCard>
                                </ShortCardItem>

                                <ShortCardItem>
                                    <CardsLabel>Product</CardsLabel>
                                    <ShortCard>
                                        <CardText>{storageInfo.product.name}</CardText>
                                    </ShortCard>
                                </ShortCardItem>

                                <ShortCardItem>
                                    <CardsLabel>Payment Method</CardsLabel>
                                    <ShortCard>
                                        <CardText>{storageInfo.payment_method || '---'}</CardText>
                                    </ShortCard>
                                </ShortCardItem>
                            </ShortCardsRightColumn>
                        </ShortCardsArea>

                        <LongCardsArea>
                            <LongCardItem>
                                <CardsLabel>Entry Date</CardsLabel>
                                <LongCard>
                                    <CardText>{storageInfo.entry_date.slice(0, 10)}</CardText>
                                </LongCard>
                            </LongCardItem>
                            <LongCardItem>
                                <CardsLabel>Withdrawal Date</CardsLabel>
                                <LongCard>
                                    <CardText>{storageInfo.withdrawal_date.slice(0, 10)}</CardText>
                                </LongCard>
                            </LongCardItem>
                        </LongCardsArea>

                        <AnotationsArea>
                            <AnotationsLabel>Annotations: </AnotationsLabel>
                            <AnotationItem>
                                <AnotationsText>{storageInfo.annotations || '...'}</AnotationsText>
                            </AnotationItem>
                        </AnotationsArea>

                        <ButtonWithdrawArea onPress={handleButtonClick}>
                            <ButtonWithdrawText>Withdraw Now</ButtonWithdrawText>
                        </ButtonWithdrawArea>
                    </CardsArea>
                }

            </PageBody>


            <BackButton onPress={handleBackButton}>
                <BackIcon width="44" height="44" fill="#FFFFFF" />
            </BackButton>
        </Container >
    )
}
