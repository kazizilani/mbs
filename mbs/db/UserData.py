User = {
    "username": "john",
    "password": "pass",
    "name": "John Doe",
    "accounts":[
            {
                "account-title": "Emergency Savings",
                "account-type": "savings",
                "account-number": 56,
                "account-pin": 1010,
                "balance": 500,
                "interest-rate": 0.5,
                "overdraft-limit": 0,
                "daily-transaction-limit": 50,
                "today-transaction": 10,
                "per-transaction-fee": 0.02,
                "transaction-history":[
                    {
                        "transaction-type": "deposit",
                        "amount": 20
                    },
                    {
                        "transaction-type": "withdraw",
                        "amount": 30
                    },
                    {
                        "transaction-type": "transfer",
                        "amount": 10
                    },
                ]

            },
             {
                "account-title": "Daily Spendings",
                "account-type": "savings",
                "account-number": 56,
                "account-pin": 1011,
                "balance": 200,
                "interest-rate": 0,
                "overdraft-limit": 300,
                "daily-transaction-limit": 30,
                "today-transaction": 5,
                "per-transaction-fee": 0.01,
                "transaction-history":[
                    {
                        "transaction-type": "deposit",
                        "amount": 10
                    },
                    {
                        "transaction-type": "transfer",
                        "amount": 20
                    },
                    {
                        "transaction-type": "transfer",
                        "amount": 14
                    },
                ]

            },
        ]
}