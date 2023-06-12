pragma solidity ^0.8.7;

import "hardhat/console.sol";

contract CryptoBook {
    // owner DAD
    address owner;

    event LogBookFundingReceived(address addr, uint amount, uint contractBalance);

    constructor() {
        owner = msg.sender;
    }

    // define Kid
    struct Book {
        address payable walletAddress;
        string name;
        uint releaseTime;
        uint amount;
        bool canWithdraw;
    }

    Book[] public books;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can add book");
        _;
    }

    // add book to contract
    function addBook(address payable walletAddress, string memory name, uint releaseTime, uint amount, bool canWithdraw) public onlyOwner {
        books.push(Book(
            walletAddress,
            name,
            releaseTime,
            amount,
            canWithdraw
        ));
    }

    function balanceOf() public view returns(uint) {
        console.log(uint256(0));
        return address(this).balance;
    }

    //deposit funds to contract, specifically to a kid's account
    function deposit(address walletAddress) payable public {
        addToBooksBalance(walletAddress);
    }

    function addToBooksBalance(address walletAddress) private {
        for(uint i = 0; i < books.length; i++) {
            if(books[i].walletAddress == walletAddress) {
                books[i].amount += msg.value;
                emit LogBookFundingReceived(walletAddress, msg.value, balanceOf());
            }
        }
    }

    function getIndex(address walletAddress) view private returns(uint) {
        for(uint i = 0; i < books.length; i++) {
            if (books[i].walletAddress == walletAddress) {
                return i;
            }
        }
        return 999;
    }

    //  checks if able to withdraw
    function availableToWithdraw(address walletAddress) public returns(bool) {
        uint i = getIndex(walletAddress);
        require(block.timestamp > books[i].releaseTime, "You cannot withdraw yet");
        if (block.timestamp > books[i].releaseTime) {
            books[i].canWithdraw = true;
            return true;
        } else {
            return false;
        }
    }

    // withdraw money
    function withdraw(address payable walletAddress) payable public {
        uint i = getIndex(walletAddress);
        require(msg.sender == books[i].walletAddress, "You must be the kid to withdraw");
        require(books[i].canWithdraw == true, "You are not able to withdraw at this time");
        books[i].walletAddress.transfer(books[i].amount);
    }

}