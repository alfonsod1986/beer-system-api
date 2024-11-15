from fastapi import status

def test_get_all_orders(client, mock_order_repository, domain_orders):
  response = client.get("/v1/orders")
  orders = response.json()

  assert response.status_code == status.HTTP_200_OK
  assert isinstance(orders, list)
  assert len(orders) == 3
  
  orders_dict = [o.to_dict() for o in domain_orders]

  print(len(orders[0].keys()), "==", len(orders_dict[0].keys()))
  for k in orders[0].keys():
    print("KEY:", k)
    print (orders[0][k], "==", orders_dict[0][k])
    print(orders[0][k] == orders_dict[0][k])
    print("-" * 50)
  assert orders == [o.to_dict() for o in domain_orders]
  mock_order_repository.get_all.assert_called_once()