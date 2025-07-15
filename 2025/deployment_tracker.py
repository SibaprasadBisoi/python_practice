deployments= {
    "dev" : {
        "web" : "1.2.0",
        "api" : "2.1.1",
        "db"  : "12.0"
    },
    "qa" : {
        "web" : "1.2.0",
        "api" : "2.1.1",
        "db"  : "12.0"
    },
    "prod"
        "dev" : {
        "web" : "1.2.0",
        "api" : "2.1.1",
        "db"  : "12.0"
    }
}
components = ["web", "api", "db" ]
print("Application deployment status\n")
print(f"{'component':<10} {'Dev':<10} {'qa':<10} {'prod':<10}")
print("-" * 40)

