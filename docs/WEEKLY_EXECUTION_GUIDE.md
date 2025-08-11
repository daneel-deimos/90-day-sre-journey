# 90-Day SRE Learning Plan: Weekly Execution Guide

## Time Allocation Framework
**Daily commitment: 3-4 hours (flexible based on week)**
- **Theory**: 20% (reading, videos, documentation)
- **Practical**: 50% (hands-on labs, coding, tool implementation)
- **Management**: 20% (leadership skills, team dynamics, communication)
- **Reflection/Documentation**: 10% (portfolio building, notes, blog posts)

---

## PHASE 1: FOUNDATION (Weeks 1-4)
### Focus: Core SRE principles, Linux fundamentals, and basic monitoring

### Week 1: SRE Principles & Philosophy
**Goal**: Understand SRE methodology and establish learning environment

**Theory (5 hours)**
- Read Google SRE Book Chapters 1-4 (Introduction, SRE Principles)
- Watch Google's SRE Fundamentals course (first 2 modules)
- Study SLIs, SLOs, and Error Budgets concepts

**Practical (12 hours)**
- Set up learning environment (Linux VM, GitHub repo for projects)
- Install basic monitoring tools (Prometheus, Grafana) locally
- Create first Python automation script for a current repetitive task

**Management (4 hours)**
- Research SRE team structures (embedded vs. centralized)
- Study blameless postmortem examples from Google
- Draft initial thoughts on how SRE could benefit your organization

**Deliverable**: 
- Blog post: "Understanding SRE: A Software Engineer's Perspective"
- GitHub repo with environment setup documentation
- Present 5-slide deck to management on "What is SRE and Why It Matters"

---

### Week 2: Linux Systems & Networking Deep Dive
**Goal**: Strengthen Linux fundamentals and networking knowledge

**Theory (4 hours)**
- MIT's Missing Semester (shell tools, data wrangling sections)
- Linux performance analysis fundamentals
- TCP/IP, DNS, HTTP/HTTPS deep dive

**Practical (14 hours)**
- Master Linux diagnostic tools (tcpdump, netstat, strace, perf)
- Practice troubleshooting performance issues on Linux VM
- Build shell scripts for system health checks

**Management (3 hours)**
- Understand on-call rotation best practices
- Study incident commander role and responsibilities

**Deliverable**:
- Linux troubleshooting runbook with 10 common scenarios
- Automated health check script with documentation
- Demo to team: "Linux Performance Troubleshooting in 15 Minutes"

---

### Week 3: Monitoring & Observability Basics
**Goal**: Implement basic monitoring using Prometheus and Grafana

**Theory (4 hours)**
- Four Golden Signals (latency, traffic, errors, saturation)
- Time-series data and PromQL basics
- Observability vs. monitoring concepts

**Practical (14 hours)**
- Deploy Prometheus + Grafana stack
- Create dashboards for a sample application
- Implement basic alerting rules
- Monitor your current application (if possible)

**Management (3 hours)**
- Learn to define SLOs with stakeholders
- Practice translating technical metrics to business impact

**Deliverable**:
- Working monitoring stack with custom dashboards
- SLO definition document for one service
- Present monitoring dashboard to management with business metrics

---

### Week 4: Python for SRE & Basic Automation
**Goal**: Leverage programming skills for SRE automation

**Theory (3 hours)**
- Python libraries for SRE (os, sys, subprocess, paramiko, boto3)
- Automation best practices and patterns

**Practical (15 hours)**
- Build 3 automation scripts:
  - Log analyzer with pattern detection
  - Automated backup verification
  - Cloud resource audit tool
- Integrate scripts with monitoring alerts

**Management (3 hours)**
- Calculate toil reduction from automation
- Create automation priority matrix

**Deliverable**:
- Python automation toolkit (3-5 scripts) on GitHub
- Toil reduction report showing time saved
- Live demo: "Automating Away 2 Hours of Daily Toil"

---

## PHASE 1 CHECKPOINT
**Skills Validated**:
- [ ] Can explain SRE principles and error budgets
- [ ] Comfortable with Linux troubleshooting
- [ ] Basic monitoring stack operational
- [ ] Created first automation scripts

---

## PHASE 2: TECHNICAL MASTERY (Weeks 5-8)
### Focus: Cloud platforms, container orchestration, and advanced monitoring

### Week 5: Cloud Platform Fundamentals (AWS/GCP)
**Goal**: Establish cloud platform proficiency

**Theory (4 hours)**
- Cloud architecture patterns for reliability
- AWS/GCP core services for SRE
- Cost optimization strategies

**Practical (14 hours)**
- Deploy monitoring stack to cloud
- Implement auto-scaling based on metrics
- Create cloud resource inventory scripts
- Practice with AWS Free Tier or GCP free credits

**Management (3 hours)**
- Cloud cost management strategies
- Capacity planning fundamentals

**Deliverable**:
- Cloud-deployed monitoring solution
- Cost optimization recommendations document
- Present: "Migrating Our Monitoring to the Cloud"

---

### Week 6: Kubernetes Fundamentals
**Goal**: Container orchestration basics building on Docker knowledge

**Theory (5 hours)**
- Kubernetes architecture and components
- Pod, Service, Deployment concepts
- Kubernetes SRE challenges

**Practical (13 hours)**
- Deploy applications to local Kubernetes (minikube/kind)
- Implement health checks and readiness probes
- Create Kubernetes manifests for monitoring stack
- Practice kubectl troubleshooting

**Management (3 hours)**
- Kubernetes adoption strategies
- Container security considerations

**Deliverable**:
- Kubernetes-deployed sample application
- Kubernetes troubleshooting guide
- Demo: "Kubernetes Self-Healing in Action"

---

### Week 7: Infrastructure as Code with Terraform
**Goal**: Automate infrastructure provisioning

**Theory (3 hours)**
- IaC principles and benefits
- Terraform basics and HCL syntax
- State management best practices

**Practical (15 hours)**
- Create Terraform modules for:
  - Monitoring infrastructure
  - Basic web application stack
  - Kubernetes cluster (if using cloud)
- Implement CI/CD for infrastructure

**Management (3 hours)**
- IaC governance and approval processes
- Disaster recovery planning

**Deliverable**:
- Terraform modules repository
- Infrastructure documentation (architecture diagrams)
- Present: "Infrastructure as Code: From Click-Ops to Git-Ops"

---

### Week 8: Advanced Observability & LGTM Stack
**Goal**: Implement comprehensive observability

**Theory (3 hours)**
- Logs, Metrics, and Traces correlation
- LGTM stack architecture (Loki, Grafana, Tempo, Mimir)
- Distributed tracing concepts

**Practical (15 hours)**
- Deploy complete LGTM stack
- Implement distributed tracing
- Create correlation between logs and metrics
- Build SLO-based dashboards and alerts

**Management (3 hours)**
- Observability strategy for microservices
- Alert fatigue prevention

**Deliverable**:
- Full observability platform deployment
- SLO dashboard with error budget tracking
- Workshop: "End-to-End Observability Demo"

---

## PHASE 2 CHECKPOINT
**Skills Validated**:
- [ ] Cloud platform operational knowledge
- [ ] Kubernetes deployment and troubleshooting
- [ ] Infrastructure automation with Terraform
- [ ] Advanced monitoring implementation

---

## PHASE 3: PRODUCTION READINESS (Weeks 9-12)
### Focus: Incident management, advanced automation, and leadership skills

### Week 9: Incident Management & Response
**Goal**: Master incident response and postmortem processes

**Theory (4 hours)**
- Incident response frameworks
- Communication during incidents
- Postmortem best practices

**Practical (13 hours)**
- Create incident response runbooks
- Implement automated incident creation
- Build incident command dashboard
- Run incident simulation exercise

**Management (4 hours)**
- Lead mock incident response
- Facilitate blameless postmortem

**Deliverable**:
- Incident response framework document
- Automated incident tooling
- Lead actual/simulated incident with postmortem

---

### Week 10: CI/CD & Progressive Delivery
**Goal**: Implement SRE-integrated deployment pipelines

**Theory (3 hours)**
- Progressive delivery strategies
- Canary deployments and feature flags
- Automated rollback strategies

**Practical (15 hours)**
- Build CI/CD pipeline with:
  - Automated testing gates
  - SLO-based promotion criteria
  - Automated rollback triggers
- Implement blue-green deployments

**Management (3 hours)**
- Release management strategies
- Balancing velocity with reliability

**Deliverable**:
- Production-grade CI/CD pipeline
- Deployment safety checklist
- Demo: "Safe Deployments with Automated Rollbacks"

---

### Week 11: Service Mesh & Advanced Kubernetes
**Goal**: Implement advanced traffic management and security

**Theory (3 hours)**
- Service mesh concepts (Istio/Linkerd comparison)
- mTLS and zero-trust networking
- Advanced Kubernetes patterns

**Practical (15 hours)**
- Deploy Linkerd service mesh
- Implement traffic splitting
- Configure automatic retries and circuit breakers
- Advanced Kubernetes operators

**Management (3 hours)**
- Microservices governance
- Service mesh adoption strategies

**Deliverable**:
- Service mesh implementation
- Traffic management playbook
- Present: "Improving Reliability with Service Mesh"

---

### Week 12: Chaos Engineering & Capstone Project
**Goal**: Validate system reliability and showcase all skills

**Theory (2 hours)**
- Chaos engineering principles
- Failure injection strategies

**Practical (16 hours)**
- Implement chaos experiments
- Build gameday scenarios
- Complete capstone project combining all learned skills:
  - Fully monitored application
  - Automated infrastructure
  - CI/CD with safety checks
  - Incident response automation
  - Chaos testing results

**Management (3 hours)**
- Present comprehensive SRE transformation plan
- Define team hiring and training needs

**Deliverable**:
- Chaos engineering report with findings
- Complete SRE platform demonstration
- Executive presentation: "90-Day SRE Journey and Roadmap Forward"

---

## FINAL CHECKPOINT
**Skills Validated**:
- [ ] Production-grade monitoring and observability
- [ ] Automated infrastructure and deployments
- [ ] Incident management leadership
- [ ] Service mesh and advanced patterns
- [ ] Chaos engineering and reliability testing

---

## Weekly Schedule Template

### Monday (1.5 hours)
- Theory: Reading/video learning
- Weekly goal setting

### Tuesday (3-4 hours)
- Practical: Major project work
- Tool implementation

### Wednesday (1.5 hours)
- Management: Leadership topics
- Team/stakeholder interaction

### Thursday (3-4 hours)
- Practical: Hands-on labs
- Coding/automation

### Friday (2 hours)
- Integration work
- Documentation
- Deliverable preparation

### Weekend (3-4 hours, flexible)
- Deep practice
- Catch-up time
- Portfolio work

---

## Portfolio Building Throughout

### GitHub Repository Structure
```
/90-day-sre-journey
  /week-01-sre-fundamentals
  /week-02-linux-mastery
  /week-03-monitoring-basics
  ...
  /projects
    /monitoring-stack
    /automation-toolkit
    /incident-response
    /capstone-project
  /documentation
  /presentations
```

### Blog Post Schedule (1 per week)
- Week 1: "Understanding SRE: A Developer's Perspective"
- Week 2: "Linux Troubleshooting for SRE"
- Week 3: "Building Your First Monitoring Stack"
- Week 4: "Automating Toil with Python"
- Week 5: "Cloud Reliability Patterns"
- Week 6: "Kubernetes for SRE"
- Week 7: "Infrastructure as Code Journey"
- Week 8: "Observability vs Monitoring"
- Week 9: "Incident Response Lessons"
- Week 10: "Safe Deployment Strategies"
- Week 11: "Service Mesh Benefits"
- Week 12: "90-Day SRE Transformation"

---

## Success Metrics

### Technical Proficiency
- Deploy and operate production-grade monitoring
- Automate infrastructure provisioning
- Implement SLOs with error budget tracking
- Lead incident response effectively

### Management Readiness
- Define SRE strategy for organization
- Build team hiring criteria
- Create training programs
- Communicate value to executives

### Cultural Impact
- Establish blameless postmortem culture
- Implement 50/50 toil reduction
- Drive automation-first mindset
- Foster cross-team collaboration

---

## Calendar Integration Plan

Once approved, we'll create calendar events with:
- Daily learning blocks (with specific topics)
- Weekly deliverable deadlines
- Mock incident response sessions
- Stakeholder presentation slots
- Study group/community events
- Certification exam targets

Each calendar event will include:
- Learning objectives
- Resource links
- Deliverable reminders
- Time allocation (theory/practical/management)