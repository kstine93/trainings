# Software Engineering Fundamentals - Pt. 1
O'Reilly Training led by Nathaniel Schutta
Starting May 23, 2023

---

## Book recommendations
- Dale Carnegie: How to win friends and influence people**
- The Pragmatic Programmer


---

## What you learn
- Comp sci programs typically focus on theory to prep you for graduate work
    - Nathaniel says that undergrad degrees might put you ahead for "a year or two" but that things tend to even-out eventually
- Boot camps are typically more focused on the current up-and-coming frameworks
- A lot of people are self-taught and have a mix - or whatever they found interesting

---

## What you don't learn
- Writing code is a communication method
    - communicating primarily with other programmers
    - communicating secondarily with compilers & computers
- How to *read code* - **you'll spend much more time reading code than writing**
- How to work with legacy code
- **Never apologize for how you became a developer - if you have the mindset, you have it.**
- Writing code is a creative process - building something.
- Being open and honest about the bugs you make and what's going on will help you and others learn - foster an ego-less culture.
- **How to work with other people**
    - How to figure out what customers *actually want*
- Perfect is the enemy of the good (don't try to do everything)
- Don't build it until you need it
- You probably won't build software that is used by most of the world - it will have relatively few users. There's no need to make it infinitely scalable or perfectly designed.
    - It's a fine line between building stuff you don't need vs. painting (coding) yourself into a corner.

---

## General advice for development
1. It's *o.k.* to start with crappy, 'brute-force' code - but clean it up afterwards.
2. The enemy to progress is "This is how we've always done it".
3. **It pays to learn Big-O notation**
4. Never underestimate the value of fresh eyes - they will see things in ways that you can't
5. Don't solution too quickly - learn first, then plan, then solve.
6. Define terms and align with the crew beforehand - make sure we're painfully, bored-out-of-our-minds clear about what we're doing and what we're solving.
7. GET MORE SLEEEEP. Your brain needs it to solve that problem. Long nights won't solve the issue - they'll cause more harm often. Sleep on a solution.
8. Have enough contiguous time to 'load a problem into your brain' - block out your schedule.
9. Keep your application chunky (in smaller pieces). Your brain can't load such a big program (this is the basis for microservices too).
10. Learn a language different from what you currently use
    - Something low-level like Java?
    - Something functional like Haskell?
    - Heard some good things about Ruby and GO...
11. Methods should be simple - and do ONE THING.
12. Our programs should have **high cohesion** and **low coupling**. [Read more here](https://medium.com/clarityhub/low-coupling-high-cohesion-3610e35ac4a6)
    - Things that belong together are coded together; modules have few inter-dependencies.
13. Favor composition over inheritance
    - There are very few true inheritance patterns - most child classes actually only need SOME of the code in the parent class - not all.
    - Instead of classes inheriting other classes as a way to share functionality, instead have the first class just include an **instance** of the second class as a class variable.
    - [read more here](https://medium.com/geekculture/composition-over-inheritance-7faed1628595)
14. Code to the **interface** not the **implementation**
    - i.e., we should be able to change how a method is implemented without worrying about where that method is called.
15. Limit comments - [read comment best practices](https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/)

16. Make sure you have tests for all of your code
    - See if you can use a plugin for identifying what code I don't have coverage for [like this](https://marketplace.visualstudio.com/items?itemName=markis.code-coverage)
17. Look into source code analysers [like this one](https://quintagroup.com/cms/python/pylint#)
    - When you use a code analyser, only turn on a few rules at a time - and don't turn on ALL of them.
18. Be critical of the code, **not the people who wrote the code**.
    - Open up your codebase for others to review
    - Try not to tie your self-worth the worth of your code.
19. There's a difference between **essential complexity and accidental complexity**
    - The former is necessary - because what we're making is complex.
    - The latter is unneeded - it's a too-fancy or too roundabout implementation. It makes our job harder.
20. Code will live longer than you expect it to (and longer than it should).

---

## General advice for workplaces
1. If you want to introduce change to a workplace:
    1. Introduce it as an 'experiment'
    2. Timebox the experiment
    3. Give leads a "emergency brake" option so they feel in control
    4. Pomodoro technique:
        1. Work for 25 minutes on a single task (set a timer) - if you have any other to-dos pop up, just jot them down.
        2. Take a 5-minute break (set a timer)
        3. Do 4 of these (2 hours)
        4. Take a longer break (30 mins)
2. To learn about a codebase:
    1. Talk to the team
    2. Read the documentation!
        - If there is no documentation, write your own!
    3. Look at the code
    4. Read the tests

---

## Writing good documentation
1. Assume people know very little
2. Provide contact information
3. Provide FAQs
4. Provide glossary
5. Show date of the last time the documentation was updated

---

## To Do:
1. Get more experience *reading code*
    1. Look at Trending projects on Github
    2. Look at React (JS)
