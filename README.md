# Case-35-The_miners_dilemma

<font face = Times size=4>

***Backgrounds:***

An open distributed system can be secured by requiring participants to present proof of work and rewarding them for participation. The Bitcoin digital currency introduced this mechanism, which is adopted by almost all contemporary digital currencies and related services.

A natural process leads participants of such systems to form pools, where members aggregate their power and share the rewards. Experience with Bitcoin shows that the largest pools are often open, allowing anyone to join. It has long been known that a member can sabotage an open pool by seemingly joining
it but never sharing its proofs of work. 
<font face = Times size=4 color = 'red'>
*The pool shares its revenue with the attacker, and so each of its participants earns less.* </font>

</font>

<font face = Times size=4>

***Game Formulation:***

In the paper, the authors define and analyze a game where pools use some of their participants to infiltrate other pools and perform such an attack. With any number of pools, no-pool-attacks is not a Nash equilibrium. They study the special cases where either two pools or any number of identical pools play the game and the rest of the participants are uninvolved. In both of these cases there exists an equilibrium that constitutes a tragedy of the commons where the participating pools attack one another and earn less than they would have if none had attacked. 

<font face = Times size=4 color = 'red'> *For two pools, the decision whether or not to attack is the miner’s dilemma, an instance of the iterative prisoner’s dilemma.* </font>  The game is played daily by the active Bitcoin pools, which apparently choose not to attack. If this balance breaks, the revenue of open pools might diminish, making them unattractive to participants.

</font>

<div align="center">
<a href="https://sm.ms/image/7Cpvyw3xOqQ8NoD" target="_blank"><img src="https://i.loli.net/2021/07/07/7Cpvyw3xOqQ8NoD.png" ></a>
    </div>

<font face = Times size = 3>
    <center> Fig1: Two pools infiltrating each other </center>
    </font>

<font face = Times size=4>

In this scenario we have pool 1 of size $m_{1}$ and pool 2 of size $m_{2}$; pool 1 controls its infiltration rate $x_{1,2}$ of pool 2, but now pool 2 also controls its infiltration rate $x_{2,1}$ of pool 1. 

</font>

<font face = Times size=4>

***The Prisoner's Dilemma:***

In a healthy Bitcoin environment, <font face = Times size=4 color = 'red'> 
*where neither pool controls a strict majority of the mining power, both pools will earn less at equilibrium than if both pools ran without attacking.* </font> We can analyze in this case a game where each pool chooses either to attack and optimize its revenue, or to refrain from attacking.

Consider pool 1 without loss of generality. As we have seen in Section $\mathrm{V}$, if pool 2 does not attack, pool 1 can increase its revenue above 1 by attacking. If pool 2 does attack but pool 1 does not, we denote the revenue of pool by $\tilde{r}_{1}$. The exact value of $\tilde{r}_{1}$ depends on the values of $m_{1}$ and $m_{2}$, but it is always smaller than one. As we have seen above, if pool 1 does choose to attack, its revenue increases, but does not surpass one. The game is summarized in Figure 2 below.

</font>

<div align="center">
<a href="https://sm.ms/image/ZhTag2ukHiJEp5c" target="_blank"><img src="https://i.loli.net/2021/07/07/ZhTag2ukHiJEp5c.png" ></a>
    </div>

<font face = Times size = 3>
Fig2: Prisoner’s Dilemma for two pools. The revenue density of each pool is determined by the decision of both pools whether to attack or not. The dominant strategy of each player is to attack, however the payoff of both would be larger if they both refrain from attacking.
    </font>
    
<font face = Times size=4>

When played once, this is the classical prisoner’s dilemma. Attack is the dominant strategy: Whether pool 2 chooses to attack or not, the revenue of pool 1 is larger when attacking than when refraining from attack, and the same for pool 2. At equilibrium of this attack-or-don’t game, when both pools attack, the revenue of each pool is smaller than its revenue if neither pool attacked.

However, the game is not played once, but rather continuously, forming a super-game, where each pool can change its strategy between attack and no-attack. The pools can agree (even implicitly) to refrain from attacking, and in each round a pool can detect whether it is being attacked and deduce
that the other pool is violating the agreement. In this supergame, cooperation where neither pool attacks is a possible stable state (**Pareto optimality**), despite the fact that **the single Nash equilibrium in every round is to attack.**

</font>
