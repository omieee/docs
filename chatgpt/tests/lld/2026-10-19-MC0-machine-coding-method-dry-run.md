# MC0 machine-coding method: teaching and dry-run record

- Date: 2026-10-19 IST (exact lesson start/end and active minutes not established).
- Week: W3 (Oct 19-25), Phase1_Master_Plan_v3.4.
- Teacher: ChatGPT. MC1 invigilator/verifier: Claude.
- Status: METHOD TAUGHT; GUIDED TEXT DRY RUN COMPLETE; NO FORMAL UNIT VERDICT.
- Evidence: This MC0 ChatGPT conversation. No MC0 code, tests, CI, timed rep, recorded voice proof, or independent executable artifact.
- Planning: MC0 is a proposed 1.5-hour GAP before MC1, NOT in approved v3.4 section 14. The instruction was a 90-minute teaching box, 135-minute hard stop absent Om extension; elapsed active minutes are UNKNOWN and must not be invented.
- The Sept 28 Parking Lot work was AI-assisted practice, not an eligible 90-minute MC rep.
- No Snake and Ladder mechanics, code, or editorial were supplied. L1 OOP pillars, SOLID, patterns, UML and concurrency were not taught.
- Rubric covered: six criteria 0-2: runs end to end; domain model; minute-60 new requirement/extensibility; readability; tests; concurrency if requested. Passing MC1 needs end-to-end running and >=8/12. Prioritize running code.
- Interview time-split discussed: requirements 5-10m, design 10-15m, code 60-75m with minute-60 change, demo/final check 5-10m. Working core first, no AI outside the permitted rep.
- Resource: workat.tech 'What is a Machine Coding Round?' named; no fresh same-day beginner video verification demonstrated in this chat. Do not mark it as an independently verified video lesson.

## Verbatim responses and corresponding prompts

The response lines below reproduce Om's typed answers, including original spelling, punctuation and wording. Affirmations are included when they marked a step as clear. Coach teaching in between is summarized (not treated as Om's independent statements).

### Stage 0: starting baseline

**Coach prompt:** "Suppose you're given a Parking Management System problem. How do you decide which classes to create, and which responsibilities belong to each class? Explain your current thought process. This is not scored."

**Om (verbatim):**
> I would think of classes like vehicle (with all details in it including parking details) and a parking lot class (with slots ) so a vehicle class that has type (if I try to feel exautic then would also create an enum and struggle with syntax) and also has which parking lot number Attica red and what is the entry time … I would also go ahead and create a parking lot class with size that it can hold (again an exotic enum) with status (exotic enum) … the reason I am telling exotic because I think simple string hardcoded status will also work … and while exit will get the input time and calculate the bill so for hourly rate I may create a simple data class that will hold just s dictionary… yeah I think I would go this first

**Teaching/intervention:** Named the difference between requirements and class syntax. Used a library borrow/return illustration before bringing the question back to parking.

**Coach assessment (not a score):** Identifies natural objects and fields (vehicle type, entry time, slot, availability, tariff). Initial default is to name classes, Enums and dictionaries before stating observable requirements; class responsibilities and boundaries were not yet clear. Om explicitly recognized plain strings could be sufficient. Do not treat Enum syntax as a demonstrated skill gap requiring extra MC0 curriculum.

### Stage 1: requirements and clarification

**Coach prompt:** "For your Parking Management System, write the first 3 things your program must be able to demonstrate to the interviewer. Just three simple statements."

**Om (verbatim):**
> 1) A car will come near parking gate collect the ticket
> 2) will park the car in it’s assigned space . This making it unavailable
> 3) at exit pay the amount based on hour of stay and make the space available again

**Coach teaching:** Clarified these as entry/ticket/assignment, occupancy, exit/fee/payment/release; introduced the all-slots-full gap.

**Coach prompt:** "Suppose a car arrives and every parking slot is occupied. As a candidate, what would you say or ask the interviewer about this situation before you start coding?"

**Om (verbatim):**
> What will happen when a car coed to the entry gate and all slots are full ?

**Coach teaching:** Gave the more precise question: reject immediately or queue? Supplied fictional interviewer answer: reject, do not issue ticket; added that to spec. Distinguished WHAT a program must do from HOW it implements it.

**Coach prompt:** "Is this distinction clear?"

**Om (verbatim):**
> Yes

**Coach assessment:** Correct three happy-path behaviors and a sensible clarification question, after being prompted with the full-lot scenario. Did not independently enumerate failure cases before the coach raised them. Shows understanding of requirements vs implementation after explanation.

### Stage 2: class boundaries and responsibilities

**Coach prompt:** "Using the four requirements we established, which classes would you create, and what single main responsibility would you assign to each?"

**Om (verbatim):**
> Vehicle and parking lot

**Coach prompt:** "Vehicle: What information should it hold, and what should it do? ParkingLot: What information should it hold, and what should it do?"

**Om (verbatim):**
> Vehicle; it’s details, it’s parking place and entry time
> Parking lot: what type of vehicle it can hold, is it vacant 

**Coach teaching:** Differentiated a ParkingLot (collection/coordination) from a ParkingSlot (individual availability/compatibility) using three slots. Noted a dictionary in ParkingLot is also possible; no automatic need for a third class.

**Coach prompt:** "Suppose a car arrives. We have S1 occupied and S2 available. Which class should be responsible for finding S2 and assigning it to the car, and why?"

**Om (verbatim):**
> Yes there should be manager class that gets input of incomin vehicle and based on it’s type it should search parking slot and assign a ticket and slot to it

**Coach teaching:** Confirmed the coordination responsibility. Explained that ParkingLot itself could manage assignment in a small implementation, without automatically creating a ParkingManager.

**Coach prompt:** "Is this distinction clear?"

**Om (verbatim):**
> Yes

**Coach assessment:** Initial responses described DATA but did not identify BEHAVIOR/ownership when asked. After the example, Om correctly introduced a coordinator that matches vehicle type, finds a compatible slot and issues a ticket. A distinct Manager class was proposed, but whether it is needed is an implementation trade-off. This was coached, not independent cold design proof.

### Stage 3: coding priority

**Coach prompt:** "Suppose you've finished the class design and have only 30 minutes left to code. Would you first implement all the class attributes and supporting structures, or implement one complete car-entry-to-exit flow? Tell me what you'd code first and why."

**Om (verbatim):**
> First a full working flow … because working code or at least working happy path is more important 

**Coach teaching:** Confirmed the complete flow is the first milestone, but alone does not meet MC1 rubric; actual execution and tests still matter.

**Coach assessment:** Correct independent verbal prioritization. No executable timed implementation observed, so cannot infer coding speed or code quality.

### Stage 4: change introduced at minute 60

**Coach scenario:** "New requirement: Parking is free for the first 15 minutes. After that, charge according to the existing hourly rate."

**Coach prompt:** "Which part of your system would you modify? Which parts would you leave untouched?"

**Om (verbatim):**
> 1. I will change the bill calulation part 
> 2. I will not change anything else allocation, deallocation every thing else remains same

**Coach teaching:** Confirmed localized billing change; supplied the example of clarifying whether 16 minutes means one full hour or starts a billable duration after the 15-minute grace period. The coach, not Om, raised that rate-boundary ambiguity.

**Coach prompt:** "Is this clear?"

**Om (verbatim):**
> yes

**Coach assessment:** Correctly isolates a pricing change from allocation and release, without hints about the component. Actual extensibility under timed code change remains unproven; no independently proposed edge-case clarification was demonstrated here.

### Stage 5: demonstration and proof of behavior

**Coach prompt:** "Imagine your Parking Management System has only two parking slots, both initially available. Give me a sequence of 4–5 operations you would demonstrate to convince the interviewer your system works correctly."

**Om (verbatim):**
> Park Veh 1 in Slot 1 -> Parked
> Park Veh 2 in Slot 2 -> Parked
> Park Veh 3 in Slot 2 -> Reject (Slot is already full)
> Un Park Veh 1 in Slot 1 -> Vacant 
> Park Veh 3 (if he is still around) in Slot 1 -> Parked
> Un Park Veh 3 -> Vacant
> Un Park Veh 2 -> Vacant

**Coach teaching:** Noted that the rejected third vehicle should be rejected because the lot has no compatible space, not merely because requested Slot 2 is occupied. Noted lack of demonstrated fee, payment outcome and duration, despite those being earlier requirements. Illustrative amount was given by coach, not Om.

**Coach prompt:** "How can you prove that Vehicle 1's slot wasn't made available before its payment succeeded?"

**Om (verbatim):**
> Once the payment is received after that only the slot will be marked is vacant 

**Coach teaching:** Contrasted 'asserting a rule' with 'demonstrating it'. Supplied failure-then-success trace: payment FAILED => slot remains OCCUPIED; payment SUCCESS => slot becomes AVAILABLE. No independent re-demonstration followed.

**Coach assessment:** Strong intuitive state-transition testing: full lot, release/reuse, multiple vehicles. Missing original billing/payment demonstration and payment-failure negative case. On follow-up, Om stated the desired invariant but supplied no operation sequence proving it. The failure/success test was teacher-provided. This is the clearest remaining gap: independently constructing evidence that a rule holds, rather than asserting it.

## Summary: teacher's opinion and rationale

**Recommendation:** Proceed to MC1 as the planned DIAGNOSTIC, without pre-teaching Snake and Ladder or adding new prerequisites. Om knows the method well enough to attempt an independent rep; this is a readiness-to-attempt recommendation, NOT a prediction of passing it.

**Positive evidence:** (a) quickly named the main data; (b) specified correct happy-path requirements; (c) asked about full capacity when scenario was posed; (d) after a concrete example, recognized allocation coordination; (e) independently prioritized running code; (f) cleanly isolated pricing modification; (g) described a meaningful sequence of occupancy/reuse states.

**Observed gaps, in order:**
1. Starts by selecting classes and 'exotic' syntax before fixing executable requirements.
2. Happy path comes first; missing/error requirements emerge only when prompted.
3. Initially lists attributes instead of responsibilities; coordinator surfaced after coaching.
4. Time/implementation priority is clear verbally but unverified by code.
5. Correct localization of requirement change, but actual mid-round adaptation untested; fee-boundary question was teacher-supplied.
6. Verbal demo omitted billing and payment despite initial spec. Initially described an occupied requested slot instead of checking whole-lot availability. After payment-failure prompt, repeated rule rather than producing failure-case evidence; coach supplied negative test.

**DO NOT claim:** PASS, MC1 readiness proved, OOP fluency, proficiency with Python/Enum syntax, tests actually executed, effective time management under 90m, debugging ability, payment/failure handling implemented, 3-question cold interview passed, or voice proof. This lesson was a guided TEXT dry run, with no score.

**Coach/process limitations:** (1) Prior explanation incorrectly treated MC1 before L1 as itself a sequencing bug; corrected after Claude's feedback because MC1 is intentionally diagnostic. (2) No same-day checked beginner video was supplied for MC0; a resource was named and its verification claimed in an earlier reply without a visible fresh fetch in this chat. Do not record that as completed verified-video work. (3) Exact active time/mode were not captured even though Om was asked for them. (4) The session contained coaching and follow-up questions, not the formal independent section 7 proof. No new teaching curriculum should be inserted into MC1 as compensation.

## Handoff to Claude

UNIT | MC0 machine-coding method | METHOD TAUGHT (guided text only; no verdict) | EVIDENCE this record and the MC0 conversation | GAP independent behavior proof, error cases, class responsibilities and actual timed coding not established | ASK invigilate MC1 Snake and Ladder as planned, 90m uninterrupted, no AI, minute-60 change, raw notes before cleanup; run code/tests and apply exact s7 rubric; one verdict by Claude only. Pass your verified findings to ChatGPT for the 60-minute review.

MC0 amendment (+1.5h) remains proposed/unincorporated into v3.4 until Om approves a plan edit and checker passes. Active minutes remain unknown; ask Om only if needed for time logging. Avoid a score for this dry run.
