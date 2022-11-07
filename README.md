# Tokenizer Version 2

[Video comparing Tokenizer_v1 and Tokenizer_v2](https://www.youtube.com/watch?v=IZsiJJkQfkw)

### Summary

Tokenizer_v2 is superior to [Tokenizer_v1](https://github.com/ForrestChew/Tokenizer) in practically every way.
There is imporoved error handling, the GUI is responsive, the code is less convoluted, and it's created without the use
of [QtDesigner.](https://doc.qt.io/qt-6/qtdesigner-manual.html) Although a powerful tool, QtDesigner was initially
used it as a crutch to expedite the time it took to complete the project, as Tokenizer_v1 was originaly created for a hackathon.

### Improvements and changes

1. The code was rewritten from scratch to strip out the need for QtDesigner.
2. The GUI is now responsive.
3. The target image aspect ratio will be maintained when loaded into the program. In addition, an "Enlarge Image" button
   was added to give users a clear way to see their unstyled and styled image.
4. To handle errors, pop-up notification UI components were added to update users on the GUI's status.
5. The NFT minter will have to pay a fee of 0.1 ETH to mint their NFT.
6. Minting an NFT no longer awards the minter a random amount of ERC20 tokens from 1 - 15. Instead, the minter will receive
   1 ERC20 token. The reason for the random rewards generated in tokenizer_v1, was a constraint of the hackathon
   to incoporate a piece of Chainlink technology, and thus, the Chainlink VRF was used to generate on-chain randomness to select the
   amount of tokens to award a minter. In Tokenizer_v2, the Chainlink VRF was removed in favor of a more consistant reward system of
   awarding one token to the minter per NFT that they mint.
7. Both the ERC721 and ERC20 smart contracts were rewritten and moved to their own [repository](https://github.com/ForrestChew/tokenizer-v2-smart-contracts).
