# AI career options: request for Claude's independent review
Date: 2026-10-27 IST | Author: ChatGPT | Status: IDEA, not an approved amendment.

Source of truth: Phase1_Master_Plan_v3.8.md, sha256 25bb309e79a610f2b37651107d1b780cedd5e3897fd2c969fb0e2f3c4b0690a4. W4 is Oct 26-Nov 1. Structure frozen until the Nov 15 reforecast absent a genuine section 9 trigger.

## Om's actual proposal
Om expects AI infrastructure investment to turn into commercially sold services and future engineering roles. He wants knowledge before buzzwords reach his IBM team, and wants a genuine advantage, not herd-following. Two paths:
1. **AI Infrastructure Engineer**, building on Go/Python backend, Kubernetes, cloud, distributed systems and platform reliability: inference serving, scheduling, scaling, routing, observability, security, GPU efficiency, cost.
2. **Applied AI/ML Engineer**, who takes an existing base model, assesses the need for adaptation, fine-tunes when justified, evaluates, deploys and operates a reliable production solution. NOT merely wiring up a ChatGPT API; NOT pretraining frontier models from scratch.

He may watch quality mobile/YouTube lessons in free time and later pay for a worthwhile course. Hypothetical capacity of 4 study hours/day would permit 1h/day AI, but the current verified plan is around 12h/week, not 4h/day. Do not treat that hypothetical extra time as available.

## Dated evidence, without pretending it predicts hiring
- IBM announced [llm-d 1.0 on 20 Oct 2026](https://newsroom.ibm.com/2026-10-20-llm-d-1-0-advances-open%2C-cost-efficient-ai-inference-for-production-scale). IBM Research is involved in Kubernetes-native inference serving; Om has no claimed production work in that project.
- Cisco Bengaluru: [AI Infrastructure Engineer, Go/Kubernetes/Linux, 8-12y](https://cisco.wd5.myworkdayjobs.com/en-US/Cisco_Careers/job/AI-Infrastructure-Engineer---GoLang--Kubernetes--Dockers--Linux---8-12-years_2011042), and [Kubernetes AI Infrastructure, Go/Python](https://cisco.wd5.myworkdayjobs.com/en-US/Cisco_Careers/job/Kubernetes-Platform-Engineer---AI-Infrastructure---Golang-Python-----8--Years-_2013536-1).
- [Sarvam AI infrastructure platform role](https://www.sarvam.ai/careers/jobs/fcb15601-6440-41f7-aa79-b9992057a4b2) discusses GPU fleets, scheduling, inference p99 and multitenancy.
- Contrasting [Applied ML Engineer JD](https://vidman.ai/careers/applied-machine-learning-engineer/) requires dataset preparation, fine-tuning, evaluations, PyTorch, GPU memory and practical ML experience. Clearly a bigger gap for Om.
- Official engineering reference: [NVIDIA Triton architecture](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/architecture.html). These are examples, **not** a representative hiring census.

## ChatGPT's proposal (no schedule edits)
**First 4 weeks: optional, free-time-only 3-4h/week (12-16h in total), video-first, no mastery claim, no new project, no forced debt.** Anything made required must be honestly funded with added hours or displaced scope/gate dates.
- Weeks 1-2: [DeepLearning.AI AI for Everyone](https://www.deeplearning.ai/courses/ai-for-everyone), Week 1 'What is AI?' and Week 2 'Building AI Projects' (beginner, no prerequisites). [3Blue1Brown neural networks chapter 1](https://www.youtube.com/watch?v=aircAruvnKk). Selected intros to LLMs and production ML from [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/) as videos only. Full Google course has Python and math prerequisites.
- Week 3 (Path A): [IBM Research llm-d 1.0 overview](https://research.ibm.com/blog/llmd-1-0-is-ready-for-production-inference-serving) and Triton's request/scheduler/backend/response architecture. Later, [Efficiently Serving LLMs](https://www.deeplearning.ai/courses/efficiently-serving-llms), **intermediate**, not first-time code instruction.
- Week 4 (Path B): Intro and 'Why finetune?' videos in [Finetuning Large Language Models](https://www.deeplearning.ai/courses/finetuning-large-language-models), which is **intermediate** and assumes Python plus a deep learning framework. [Hugging Face LLM Course intro](https://huggingface.co/learn/llm-course/chapter1/1) as overview; its full course requires solid Python and preferably an intro ML course. If B is selected later, assess [Andrew Ng beginner ML Specialization](https://www.deeplearning.ai/specializations/machine-learning), full scope and costs, or [fast.ai lesson 1](https://course.fast.ai/Lessons/lesson1) plus practical notebooks.
- Optional 3-line reflection: new idea / link to IBM platform work / what is unclear. Watching is vocabulary exposure, not production proof.
- No purchase now. AI-infused software delivery is a workflow skill, not equivalent to either target role.

## Possible future outcomes
A: stay the main platform offer route, add measured AI serving depth when demonstrated relevant; mock inference gateway routing and latency/cost metrics (no GPU needed at start).
B: a distinct material career pivot requiring ML fundamentals, PyTorch, datasets, experiments, proper evaluation, GPU labs and model operations, probably considerably more learning and proof, not a 10-hour bolt-on.
Choice: retain v3.8 unchanged at present; assess Nov 15 with actual capacity and dated JD harvest evidence. If mandatory content is added, use full section 9 change control, run plan generator/check_plan.py, and obtain Om approval before editing master.

## Independent questions for Claude
1. Is Path A actually the right adjacency for Om's real production record, or are we overfitting recent postings?
2. Can Path B plausibly be an employable 2028 route for an engineer without recent ML production, or should this be model-literate infrastructure instead? State beginner hours and proof needed.
3. Are the named resources truly beginner-accessible in this order? Replace weak video choices with exact better lessons, and distinguish passive viewing from hands-on readiness.
4. Considering the frozen v3.8 and measured ~12h/week, is optional exposure an intelligent edge or more avoidance/fragmentation? Explain which evidence would justify formal hours.
5. Is targeted IBM collaboration with teams around inference infrastructure more valuable than a self-study toy? How should Om earn honest code ownership without inflating claims?

Please **disagree where evidence warrants**. Om and not either coach decides. Do not edit the master plan or issue a plan verdict just because this request was written.
