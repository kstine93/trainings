# Setting up basic Mongo DB Kubernetes cluster
Working off of [this video](https://youtu.be/X48VuDVv0do?t=4633)

## Planning

### Architecture

**Overview**
We are going to deploy 2 applications:
- MongoDB and Mongo-express

This will consist of a few components:
- MongoDB pod
- internal service connecting to MongoDB pod
- Mongo-express deployment referencing:
  - Url (in ConfigMap)
  - Credentials (in Secrets)
- External service allowing the internet to access our Mongo-express pod
- **Bonus:** Ingress to allow nice DNS name 