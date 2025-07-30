configs = {
    "dev": {
        "region": "us-west-1",
        "db_url": "dev-db.example.com",
        "app_version": "1.2.0-dev"
    },
    "qa": {
        "region": "us-east-2",
        "db_url": "qa-db.example.com",
        "app_version": "1.2.0-qa"
    },
    "prod": {
        "region": "eu-central-1",
        "db_url": "prod-db.example.com",
        "app_version": "1.2.0"
    }
}
env = input("Enter the environment (dev, qa, prod): ").strip().lower()
if env in configs:
    print(f"\nDeployment configuration for {env}")
    for key, value in configs[env].items():
        print(f" {key}: {value}")
else:
    print(f"Environment {env} not found in configuration")
