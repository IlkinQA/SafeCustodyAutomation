basket_schema = {
    "type": "object",
    "properties": {
        "UserId": {"type": "integer"},
        "MatrixId": {"type": "integer"},
        "MatrixName": {"type": "string"},
        "Actualized": {"type": "boolean"},
        "BasketPositions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "DetailId": {"type": "integer"},
                    "RegionId": {"type": "integer"},
                    "PartyCount": {"type": "integer"},
                    "MakerId": {"type": "integer"},
                    "MakerName": {"type": "string"},
                    "DetailGroupId": {"type": "integer"},
                    "DetailGroupName": {"type": "string"},
                    "DetailNumber": {"type": "string"},
                    "DetailName": {"type": "string"},
                    "RegionName": {"type": "string"},
                    "RegionShortName": {"type": "string"},
                    "Quantity": {"type": "integer"},
                    "QuantityOld": {"type": "integer"},
                    "InputPrice": {"type": "number"},
                    "Price": {"type": "number"},
                    "PriceOld": {"type": "number"},
                    "PriceSum": {"type": "number"},
                    "DateDelivery": {"type": "string", "format": "date-time"},
                    "Reference": {"type": "string"}
                },
                "required": ["MatrixName"]  # Укажите обязательные поля
            }
        }
    }
}