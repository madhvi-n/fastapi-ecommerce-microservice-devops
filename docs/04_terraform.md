# 🌍 Terraform

## 🔧 What is Terraform?

Terraform is an open-source Infrastructure as Code (IaC) tool by HashiCorp that allows you to define, provision, and manage infrastructure using configuration files written in HashiCorp Configuration Language (HCL).

* Declarative syntax
* Works with many cloud providers (AWS, Azure, GCP, etc.)
* Automates infrastructure creation, update, and teardown


## ✅ Why Use Terraform?

* Version-controlled infrastructure
* Consistency across environments (dev, staging, prod)
* Automate cloud resource provisioning
* Reusable and modular configurations
* Great for CI/CD and DevOps pipelines


## 🧱 Key Concepts

### 1. **Provider**

Specifies the cloud/platform Terraform will interact with (e.g., AWS, GCP, Azure).

```hcl
provider "aws" {
  region = "us-west-2"
}
```

### 2. **Resource**

Represents a piece of infrastructure like an EC2 instance, S3 bucket, etc.

```hcl
resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}
```

### 3. **Variable**

Inputs that make configuration dynamic and reusable.

```hcl
variable "region" {
  default = "us-east-1"
}
```

### 4. **Output**

Export values from Terraform (e.g., IP address, bucket URL).

```hcl
output "instance_ip" {
  value = aws_instance.example.public_ip
}
```

### 5. **State File**

Terraform keeps track of all deployed infrastructure in a `.tfstate` file to detect changes.


## 🔁 Terraform Workflow

1. **Write**: Define resources in `.tf` files
2. **Initialize**: `terraform init` to install providers
3. **Plan**: `terraform plan` to preview changes
4. **Apply**: `terraform apply` to create/update infra
5. **Destroy**: `terraform destroy` to tear down infra


## 📦 Common Terraform Commands

```bash
terraform init                # Initialize a working directory
terraform plan                # Preview changes
terraform apply               # Apply changes
terraform destroy             # Destroy infrastructure
terraform validate            # Validate configuration
terraform fmt                 # Format configuration files
terraform output              # Show output variables
```

## 🔐 Best Practices

* Use `.tfvars` for sensitive or environment-specific variables
* Never commit `.tfstate` or `.tfvars` to source control
* Use remote backends (e.g., S3 + DynamoDB for AWS) for team environments
* Organize code into modules for reuse
* Use version constraints for providers


## 📚 Learn More

* [Terraform Official Docs](https://www.terraform.io/docs/index.html)
* [Learn Terraform – HashiCorp](https://learn.hashicorp.com/terraform)
* [Terraform Registry](https://registry.terraform.io/)
* [Awesome Terraform GitHub Repo](https://github.com/shuaibiyy/awesome-terraform)
