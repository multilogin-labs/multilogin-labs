terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "github_repo" {
  description = "GitHub repo for the multilogin-labs site"
  type        = string
  default     = "multilogin-labs/multilogin-labs"
}

provider "aws" {
  region = var.region
}

# S3 bucket to host an optional mirror of the GitHub Pages output (e.g. for a custom domain).
resource "aws_s3_bucket" "pages_mirror" {
  bucket_prefix = "multilogin-labs-pages-"
  tags = {
    Project = "multilogin-labs"
    Repo    = var.github_repo
  }
}

resource "aws_s3_bucket_website_configuration" "pages_mirror" {
  bucket = aws_s3_bucket.pages_mirror.id
  index_document { suffix = "index.html" }
  error_document { key = "index.html" }
}

output "s3_bucket" {
  value = aws_s3_bucket.pages_mirror.bucket
}

output "website_endpoint" {
  value = aws_s3_bucket_website_configuration.pages_mirror.website_endpoint
}
