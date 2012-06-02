# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import datetime
##########
import GithubObject
##########
import Issue
import NamedUser

class IssueEvent( GithubObject.GithubObject ):
    @property
    def actor( self ):
        self._completeIfNotSet( self._actor )
        return self._NoneIfNotSet( self._actor )

    @property
    def commit_id( self ):
        self._completeIfNotSet( self._commit_id )
        return self._NoneIfNotSet( self._commit_id )

    @property
    def created_at( self ):
        self._completeIfNotSet( self._created_at )
        return self._NoneIfNotSet( self._created_at )

    @property
    def event( self ):
        self._completeIfNotSet( self._event )
        return self._NoneIfNotSet( self._event )

    @property
    def id( self ):
        self._completeIfNotSet( self._id )
        return self._NoneIfNotSet( self._id )

    @property
    def issue( self ):
        self._completeIfNotSet( self._issue )
        return self._NoneIfNotSet( self._issue )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def _initAttributes( self ):
        self._actor = GithubObject.NotSet
        self._commit_id = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._event = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._issue = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "actor" in attributes: # pragma no branch
            assert attributes[ "actor" ] is None or isinstance( attributes[ "actor" ], dict ), attributes[ "actor" ]
            self._actor = None if attributes[ "actor" ] is None else NamedUser.NamedUser( self._requester, attributes[ "actor" ], completed = False )
        if "commit_id" in attributes: # pragma no branch
            assert attributes[ "commit_id" ] is None or isinstance( attributes[ "commit_id" ], ( str, unicode ) ), attributes[ "commit_id" ]
            self._commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes: # pragma no branch
            assert attributes[ "created_at" ] is None or isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = None if attributes[ "created_at" ] is None else datetime.datetime.strptime( attributes[ "created_at" ], "%Y-%m-%dT%H:%M:%SZ" )
        if "event" in attributes: # pragma no branch
            assert attributes[ "event" ] is None or isinstance( attributes[ "event" ], ( str, unicode ) ), attributes[ "event" ]
            self._event = attributes[ "event" ]
        if "id" in attributes: # pragma no branch
            assert attributes[ "id" ] is None or isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "issue" in attributes: # pragma no branch
            assert attributes[ "issue" ] is None or isinstance( attributes[ "issue" ], dict ), attributes[ "issue" ]
            self._issue = None if attributes[ "issue" ] is None else Issue.Issue( self._requester, attributes[ "issue" ], completed = False )
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
