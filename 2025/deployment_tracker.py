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

for component in components:
    row = f"{component:<10}"
    for env in ["dev", "qa","prod"]:
        version = deployments.get(env, {}).get(component, "N/A")
        row+= f"{component:<10}"
    print(row)


