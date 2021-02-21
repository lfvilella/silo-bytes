from . import base


class TestStorageAPI(base.BaseTest):
    def test_list_without_login_returns_401(self):
        response = self.client.get('/api/storages/')
        self.assertEqual(response.status_code, 401)
        expected_error = {
            'detail': 'Authentication credentials were not provided.'
        }
        self.assertEqual(response.json(), expected_error)

    def test_list_returns_200(self):
        storage = self.create_fake_storage()

        silo = self.create_fake_silo()
        storage2 = self.create_fake_storage(silo=silo)

        self.authenticate()
        response = self.client.get('/api/storages/')
        self.assertEqual(response.status_code, 200)

        expected_response = [
            {
                'id': storage2.id,
                'client': {
                    'id': storage2.client.id,
                    'name': storage2.client.name,
                    'email': storage2.client.email,
                    'phone': storage2.client.phone,
                },
                'silo': {
                    'id': storage2.silo.id,
                    'name': storage2.silo.name,
                    'description': storage2.silo.description,
                    'size': float(storage2.silo.size),
                },
                'product': {
                    'id': storage2.product.id,
                    'name': storage2.product.name,
                    'description': storage2.product.description,
                },
                'annotations': storage2.annotations,
                'quantity': float(storage2.quantity),
                'price_per_day': float(storage2.price_per_day),
                'entry_date': storage2.entry_date.isoformat().replace(
                    '+00:00', 'Z'
                ),
                'withdrawal_date': storage2.withdrawal_date.isoformat().replace(  # noqa: E501
                    '+00:00', 'Z'
                ),
                'payment_method': storage2.payment_method,
                'status': storage2.status,
                'current_cost': storage2.current_cost,
                'total_cost': storage2.total_cost,
            },
            {
                'id': storage.id,
                'client': {
                    'id': storage.client.id,
                    'name': storage.client.name,
                    'email': storage.client.email,
                    'phone': storage.client.phone,
                },
                'silo': {
                    'id': storage.silo.id,
                    'name': storage.silo.name,
                    'description': storage.silo.description,
                    'size': float(storage.silo.size),
                },
                'product': {
                    'id': storage.product.id,
                    'name': storage.product.name,
                    'description': storage.product.description,
                },
                'annotations': storage.annotations,
                'quantity': float(storage.quantity),
                'price_per_day': float(storage.price_per_day),
                'entry_date': storage.entry_date.isoformat().replace(
                    '+00:00', 'Z'
                ),
                'withdrawal_date': storage.withdrawal_date.isoformat().replace(
                    '+00:00', 'Z'
                ),
                'payment_method': storage.payment_method,
                'status': storage.status,
                'current_cost': storage.current_cost,
                'total_cost': storage.total_cost,
            },
        ]
        self.assertEqual(response.json(), expected_response)
